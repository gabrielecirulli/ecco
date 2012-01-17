import re

class Parser():
    def __init__(self):
        pass
      
    def parse_http_header(self, header):
        class ParsedHeader:
            def __init__(self):
                self.header = None
                self.request = None
                self.method = None
                self.url = None
                self.version = None
                self.mime = None
        
        parsed = ParsedHeader()
        header = header.split('\r\n')
        
        request = header.pop(0)
        parsed.method, parsed.url, parsed.version = request.split(' ')
        parsed.mime = dict()
        
        for mime in header:
            temp = mime.split(': ')
            parsed.mime[temp[0]] = temp[1]
            
        return parsed
        
    def is_valid_http_header(self, header):
        valid = True
        if header == '':
            valid = False
        header = header.split('\r\n')
        firstline = header.pop(0).split(' ')
        if(len(firstline) == 3):
            if firstline[0] not in ['OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT']:
                valid = False
            if re.match('^(/|http://|\*)([a-zA-Z0-9.\-_]+(/)?)*$', firstline[1]) == None:
                valid = False
            if firstline[2] != 'HTTP/1.1':
                valid = False
        else:
            valid = False
        for line in header:
            if(len(line.split(': ')) != 2):
                valid = False
            
        return valid
        
        