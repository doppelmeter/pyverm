import serial
import socket


def type_converter(val_list: list):
    """
    Listenelemente werden in Float oder Int umgewandelt falls moeglich.
    :param val_list: Liste mit Strings
    :return: Liste mit Strings, Floats oder Integer
    """
    for i in range(len(val_list)):
        if "." in val_list[i]:
            try:
                val_list[i] = float(val_list[i])
            except ValueError:
                pass
        else:
            try:
                val_list[i] = int(val_list[i])
            except ValueError:
                pass
    return val_list


class Geocom():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.trid = 0

    def connect(self, tcp_ip="192.168.254.3", tcp_port=1212):
        self.sock.connect((tcp_ip, tcp_port))

    def request(self, rpc, *parameterlist):
        params = list()
        for element in parameterlist:
            params.append(element)
        self.trid += 1
        if self.trid > 7:
            self.trid = 1
        asciistring = "%R1Q,{},{}:{}\r\n".format(str(rpc), str(self.trid),
                                                 str(params).strip("([ ])").replace(" ", "").replace("'", ""))

        self.sock.sendall(asciistring.encode())
        data = self.sock.recv(512)[:-2]
        data_decoded = data.decode('utf-8')

        response = data_decoded.strip("%""''").split(":")
        header = type_converter(response[0].split(","))
        if len(response) > 1:
            parameter = type_converter(response[1].strip().split(","))
        else:
            parameter = "empty"
        return {"Header": header, "Parameter": parameter}

    def close(self):
        self.sock.close()

    def test_connection(self):
        pass