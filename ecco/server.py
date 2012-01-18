from ecco.basesocket import Socket

class Server(Socket):
    def __init__(self, address, port, autostart=True, bufsize=1024, backlog=5):
        Socket.__init__(self, address, port, bufsize, backlog)
        self._address = address
        self._port = port
        self._autostart = autostart
        self._bufsize = bufsize
        self._backlog = backlog
        if self._autostart:
            self.start()

    def start(self):
        self.bind()
        self.listen()

