# CODE IS STILL NOT YET FULLY DONE, IT IS ONLY ABLE TO BE ACCESED VIA YOUR LOCAL NETWORK
import socket

# DEFINE SOCKET OBJ
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ASKING USER FOR IP AND PORT OF SERVER
ip_addr = input("IP FOR SERVER: ")
html_addr = input("HTML FILE NAME[SAME DIRECTORY]: ")

# MAKING SERVER
s.bind((ip_addr, 4444))  # MAKING SERVER
print(f"SERVER STARTED ON IP:{ip_addr}, PORT: 4444")
s.listen(15)  # HOW MANY REQUESTS IT CAN HANDLE AT ONCE

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    with clientSocket:
        msg = clientSocket.recv(1024).decode()
        if msg == "HTML":
            print(f"{address} REQUESTING HTML FILE")
            # GETTING HTML DATA
            html_file = open(html_addr, "r", encoding="cp1252")
            html_file_cont = html_file.read()
            html_file.close()

            # SENDING HTML FILE
            print(str(html_file))
            clientSocket.sendall(str(html_file_cont).encode())
            print(f"SENT {html_addr} SUCCESSFULLY")
        else:
            pass
