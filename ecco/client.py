from ecco.basesocket import Socket

class Client(Socket):
    def __init__(self, address, port, autoconnect=True, bufsize=1024, backlog=5):
        Socket.__init__(self, address, port, bufsize, backlog)
        self._address = address
        self._port = port
        self._autoconnect = autoconnect
        self._bufsize = bufsize
        self._backlog = backlog
        if self._autoconnect:
            self.connect()
            
        