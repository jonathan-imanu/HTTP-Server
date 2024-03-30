import socket
import threading


CRLF = b"\r\n"
OK = b"HTTP/1.1 200 OK\r\n\r\n"
NOT_FOUND = b"HTTP/1.1 404 Not Found\r\n\r\n"

"""
HTTP Request Contents
    
GET /index.html HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1

"""

def respond(data: str) -> bytes:
    data = data.decode()
    data = data.split("\r\n")
    start_line = data[0].split(" ")
    print(start_line)
    path = start_line[1][1:]
    print(path)
    if not path.startswith("echo") and path != "":
        return NOT_FOUND
    content = path[path.find("/", path.find("/")):]
    
    
    content_type = b"Content-Type: text/plain"
    content_len = f"Content-Length: {str(len(content))}".encode()
    resp = OK + CRLF + content_type + CRLF + content_len + CRLF + content + CRLF

    return resp
    
    
    

class Server():
    # A server class to handle and respond to HTTP requests
    def __init__(self, port):
        self.port = port
    
    def run(self):
        server_socket = socket.create_server(("localhost", self.port), reuse_port=True)
        conn, addr = server_socket.accept() 
        while req := conn.recv(1024):
            resp = respond(req)
            conn.sendall(resp)

    
    def new_client(self):
        pass
        
        
        
def main():
    server = Server(4221)
    server.run()
        

if __name__ == "__main__":
    main()
