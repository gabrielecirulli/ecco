import socket


class Socket():
    """
    Wrapper class for Python Sockets (works both as server and client)
    """
    def __init__(self, address, port, bufsize=1024, backlog=5):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._address = address
        self._port = port
        self._bufsize = bufsize
        self._backlog = backlog
        
    
    def connect(self):
        self._socket.connect((self._address, self._port))
        
    
    def bind(self):
        self._socket.bind((self._address, self._port))
    
    
    def listen(self):
        self._socket.listen(self._backlog)
        
    def accept(self):
        return self._socket.accept()
    

    def close(self):
        self._socket.close()
        
    
    def send(self, data):
        if not self._connected:
            self.connect()
        return self._socket.sendall(data)
        
    
    def recv(self):
        return self._socket.recv(self._bufsize)
    
        
    def recvAll(self):
        result = ''
        while True:
            data = self.recv()
            if data != '':
                result += data
            else:
                break
        return result
        
    