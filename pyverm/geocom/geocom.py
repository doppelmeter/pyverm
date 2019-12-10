##################################################################################
# Only pyverm.geocom is under the MIT License
#=================================================================================
# MIT License
#
# Copyright (c) [2019] [Marius Hürzeler]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##################################################################################

import logging
import socket
import time

logger = logging.getLogger(__name__)



def _convert(x):
    """helper to convert variable types"""
    try:
        if "." in x:
            out = float(x)
        else:
            out = int(x)
    except:
        out = x
    return out


class geocom_connect:
    def __init__(self, *, tcp_ip="192.168.254.3", tcp_port=1212):
        """Initialise Geocom-connection"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)
        self.trid = 0
        self.tcp_ip = str(tcp_ip)
        self.tcp_port = int(tcp_port)
        self._connect(retries=20)

    def _reconnect(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        time.sleep(0.1)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)
        self._connect()

    def _connect(self, *, retries=10):
        logger.info("\tConnecting to %s (Port %s)", str(self.tcp_ip), str(self.tcp_port))
        counter = 0
        while counter < retries:
            counter += 1
            try:
                self.sock.connect((self.tcp_ip, self.tcp_port))
            except socket.timeout:
                logger.warning("\tConnecting to %s (Port %s) failed in attempt %s  \ttime out", str(self.tcp_ip),
                               str(self.tcp_port), str(counter))
                time.sleep(0.1)
            except OSError as err:
                logger.warning("\tConnecting to %s (Port %s) failed in attempt %s \t%s", str(self.tcp_ip),
                               str(self.tcp_port), str(counter), err)
                time.sleep(0.1)
            else:
                logger.info("\tTesting connection to %s (Port %s)", str(self.tcp_ip), str(self.tcp_port))
                try:
                    instrument = self.request("5004", raise_exception=True)[1]
                    serialnumber = self.request("5003", raise_exception=True)[1]
                except Exception as e:
                    logger.error(e, exc_info=True)
                else:
                    logger.info("\tConnected to Instrument %s (%s)", serialnumber, instrument)
                    return True
                    break
        self._reconnect()

    def request(self, rpc, *parameterlist, raise_exception=False):
        params = str(list(parameterlist)).strip("([ ])").replace(" ", "").replace("'", "")

        rpc = str(rpc)

        self.trid += 1
        if self.trid > 7:
            self.trid = 1

        asciistring = "%R1Q,{},{}:{}\r\n".format(rpc, str(self.trid), params)

        while True:
            counter = 0
            while counter < 2:
                counter += 1
                try:
                    self.sock.sendall(asciistring.encode())
                    trid_is_the_same = False
                    counter_2 = 0
                    while not trid_is_the_same and counter_2 < 8:
                        data = self.sock.recv(512)[:-2]
                        data_decoded = data.decode('utf-8')
                        response = data_decoded.strip("%""''").split(":")
                        trid_recv = response[0].split(",")[-1]
                        trid_is_the_same = self.trid == int(trid_recv)
                        counter_2 += 1
                    if trid_is_the_same:
                        logger.debug("\tSent: %s\tRecieved: %s", asciistring.strip(), data_decoded)
                        val_list = response[-1].strip().split(",")
                        val_list = list(map(_convert, val_list))
                        return val_list
                except socket.timeout:
                    logger.warning("\tRequest to %s (Port %s) failed \ttime out", str(self.tcp_ip), str(self.tcp_port))
                except OSError as err:
                    logger.warning("\tRequest to %s (Port %s) failed \t%s", str(self.tcp_ip), str(self.tcp_port), err)
            if raise_exception:
                raise Exception
            else:
                self._reconnect()

    def close(self):
        self.sock.close()
        logger.info("\tClose connection to %s (Port %s)", str(self.tcp_ip), str(self.tcp_port))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
