import random

from ecco.server import Server
from ecco.http import HTTP

class Core:
    @staticmethod
    def run():
        # TODO: server manager
        port = random.choice(range(50000,50010))
        server = Server('192.168.1.101', port) 
        http = HTTP()
        
        print str(port)
        
        http.run_server(server)
            
#            
#            