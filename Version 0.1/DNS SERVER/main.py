import socket
import USERCLIENT

# DEFINE SOCKET OBJ
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# BINDING IP
s.bind(("xxx.xxx.x.xxx", 4000))

# HOW MANY HANDLES AT 1 TIME
s.listen(15)

# LISTENING
while True:
    clientSocket, address = s.accept()  # ACCEPTING ANYONE WHO CONNECTS
    print(f"Connection from {address} has been established!")
    clientSocket.send(bytes("WELCOME TO M.ALI NET!!!", "utf-8"))

    # CHECKING WETHER A USER IS CONNECTING OR UNKOWN CONNECTIONS........
    request = clientSocket.recv(1024).decode()
    print(request)

    # USER HANDLING
    if request == "USER":
        USERCLIENT.user_client_conn(clientSocket, s)

    # REJECTING UNKOWN CONNECTIONS
    else:
        clientSocket.send("UNKOWN CLIENT DETECTED! DISCONNECTING FROM THE SERVER!!".encode())


