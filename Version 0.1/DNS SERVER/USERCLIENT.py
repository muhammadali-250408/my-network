import socket

import HTTPSERVERCONNECT
from JSONHANDLER import check_DNS
from HTTPSERVERCONNECT import httpServerConn

def user_client_conn (clientSocket, s):

    # GETTING THE IP
    website_request = clientSocket.recv(1024).decode() # GETTING URL THAT USER WANTS
    print(f"USER REQUESTING {website_request}") # DEBUG LINE
    output = check_DNS(website_request ) # CHECKING IF SAID URL IS IN THE JSON FILE

    # CONNECTING TO SAID IP
    html_file = HTTPSERVERCONNECT.httpServerConn(output) # CONNECTING TO THE HTTP SERVER

    # SENDING FILES
    clientSocket.sendall("HTMLINCOMING".encode())
    try:
        print(str(html_file))
        clientSocket.sendall(str(html_file).encode())# SENDING HTML FILE
        print("SUCCESFULLY SENT")
    except:
        print("HTML FILE TRANSFER FAILED")
