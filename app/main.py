import socket

CRLF = "\r\n"

def main():
    
    """
    HTTP Request Contents
    
GET /index.html HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1

    """
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    conn, addr = server_socket.accept() 
    while True:
        conn.sendall("HTTP/1.1 200 OK\r\n\r\n".encode())
        while req := conn.recv(1024):
            data = req.decode().split(CRLF)
            print(data)
            
        
        

if __name__ == "__main__":
    main()
