import socket

CRLF = "\r\n"

def main():
    print("Logs from your program will appear here!")

    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    conn, addr = server_socket.accept() 
    while True:
        conn.sendall("HTTP/1.1 200 OK\r\n\r\n".encode())


if __name__ == "__main__":
    main()
