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
        """Initialise connection"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(1)
        self.trid = 0
        self.tcp_ip = str(tcp_ip)
        self.tcp_port = int(tcp_port)
        self._connect(retries=20)

    def _reconnect(self):
        """Make a new connection if the old fails"""
        self.close()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(1)
        self._connect()

    def _connect(self, *, retries=10):
        """Connect"""
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
                    instrument = self.request("5004")[1]
                    serialnumber = self.request("5003")[1]
                except:
                    self._reconnect()
                else:
                    logger.info("\tConnected to Instrument %s (%s)", serialnumber, instrument)
                    return
        self._reconnect()

    def request(self, rpc, *parameterlist):
        """Send a Request"""
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
                    data = self.sock.recv(512)[:-2]
                except socket.timeout:
                    logger.warning("\tRequest to %s (Port %s) failed \ttime out", str(self.tcp_ip), str(self.tcp_port))

                except OSError as err:
                    logger.warning("\tRequest to %s (Port %s) failed \t%s", str(self.tcp_ip), str(self.tcp_port), err)

                else:
                    data_decoded = data.decode('utf-8')
                    logger.debug("\tSent: %s\tRecieved: %s", asciistring.strip(), data_decoded)

                    response = data_decoded.strip("%""''").split(":")
                    val_list = response[-1].strip().split(",")
                    val_list = list(map(_convert, val_list))
                    return val_list
            self._reconnect()

    def close(self):
        self.sock.close()
        logger.info("\tClose connection to %s (Port %s)", str(self.tcp_ip), str(self.tcp_port))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
