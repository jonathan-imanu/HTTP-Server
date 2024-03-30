import socket

CRLF = "\r\n"

def main():
    print("Logs from your program will appear here!")

    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    conn, addr = server_socket.accept() 
    conn.sendall("HTTP/1.1 200 OK\r\n\r\n")
    server_socket.close()


if __name__ == "__main__":
    main()
