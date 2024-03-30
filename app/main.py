import socket
import threading

CRLF = "\r\n"

"""
HTTP Request Contents
    
GET /index.html HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1

"""

def respond(data: str) -> bytes:
    start_line = data[0].split(" ")
    print(start_line)
    if start_line[1] != "/":
        return "HTTP/1.1 200 OK\r\n\r\n".encode()
    else:
        return "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    
    
    

class Server():
    # A server class to handle and respond to HTTP requests
    def __init__(self, port):
        self.port = port
    
    def run(self):
        server_socket = socket.create_server(("localhost", self.port), reuse_port=True)
        conn, addr = server_socket.accept() 
        while req := conn.recv(1024):
            data = req.decode().split(CRLF)
            resp = respond(data)
            conn.sendall(resp)
            

    
    def new_client(self):
        pass
        
        
        
def main():
    
   
    server = Server(4221)
    server.run()
        

if __name__ == "__main__":
    main()
