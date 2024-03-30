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
    data = data.split(CRLF)
    start_line = data[0].split(" ")
    unfil_content = start_line[1]
    content_idx = unfil_content.find("/", start=start_line[1].find("/"))
    content = unfil_content[content_idx:]
    encoded_content = content.encode()
    content_type = b"Content-Type: text/plain"
    content_len = f"Content-Length: {str(len(content))}".encode()
   
    resp = OK + CRLF 
    resp += content_type + CRLF
    resp += content_len + CRLF
    resp += encoded_content + CRLF
    return resp
    
    
    

class Server():
    # A server class to handle and respond to HTTP requests
    def __init__(self, port):
        self.port = port
    
    def run(self):
        server_socket = socket.create_server(("localhost", self.port), reuse_port=True)
        conn, addr = server_socket.accept() 
        while req := conn.recv(1024):
            data = req.decode()
            resp = respond(data)
            conn.sendall(resp)

    
    def new_client(self):
        pass
        
        
        
def main():
    server = Server(4221)
    server.run()
        

if __name__ == "__main__":
    main()
