import socket

CRLF = "\r\n"

"""
HTTP Request Contents
    
GET /index.html HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1

"""

class Server():
    # A server class to handle and respond to HTTP requests
    def __init__(self, port):
        self.port = port
    
    def run(self):
        server_socket = socket.create_server(("localhost", self.port), reuse_port=True)
        conn, addr = self.server_socket.accept() 
        while True:
            conn.sendall("HTTP/1.1 200 OK\r\n\r\n".encode())
            while req := conn.recv(1024):
                data = req.decode().split(CRLF)
        
        
def main():
    
   
    server = Server(4221)
    server.run()
        

if __name__ == "__main__":
    main()
