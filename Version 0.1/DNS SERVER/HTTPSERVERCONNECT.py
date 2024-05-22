import socket

def httpServerConn(IP):
    # SETTING UP SOCKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # CONNECT TO HTTP SERVER
    s.connect((IP, 4444))

    # ASK FOR HTML FILE
    s.sendall("HTML".encode())

    # RECIEVE HTML FILE
    html_file = s.recv(100000).decode()

    return html_file
