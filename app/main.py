import socket

CRLF = "\r\n"

class Server():
    def __init__(self):
        self.server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    def run(self):
        conn, addr = self.server_socket.accept() 
        while True:
            conn.sendall("HTTP/1.1 200 OK\r\n\r\n".encode())
            while req := conn.recv(1024):
                data = req.decode().split(CRLF)
        
        
def main():
    
    """
    HTTP Request Contents
    
GET /index.html HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1

    """
    server = Server
    server.run()
        

if __name__ == "__main__":
    main()
