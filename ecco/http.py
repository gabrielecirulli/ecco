import socket

from ecco.parser import Parser

class HTTP(object):
    def __init__(self):
        self._parser = Parser()
    
    
    def run_server(self, server):
        while True:
            client, address = server.accept()
            # Incoming connection, manage
            self.manage_connection(client, address)
        
        
        
    def manage_connection(self, client, address):
        # Read incoming request
        data = r''
        read = 4096
        client.setblocking(0)
        while read > 0:
            
            data += client.recv(1024)
            
            read -= 1024
            if(data.find(r'\r\n\r\n') == -1):
                break
            else:
                continue
        # Split away header
        header = data.split('\r\n\r\n')[0]
        # Drop connection if data does not contain a HTTP header
        if(len(header) == 0):
            client.close()
            return
    
        if(self._parser.is_valid_http_header(header)):
            header = self._parser.parse_http_header(header)
        else:
            # Drop connection
            client.close()
            return
        
        client.send('Hi and welcome.')
        
        # End connection
        client.close()
        return
        
        
