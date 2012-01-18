import random

from ecco.server import Server
from ecco.http import HTTP

class Core:
    @staticmethod
    def run():
        # TODO: server manager
        server = Server('192.168.1.101', 0)
        http = HTTP()

        port = server.get_port()
        print "Bound to: " + str(port)

        http.run_server(server)

#            
#
