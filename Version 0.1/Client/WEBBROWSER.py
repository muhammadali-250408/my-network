import socket


def get_html(url):
    # DEFINE SOCKET OBJ
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # CONNECT
    s.connect(("###.###.###.###", 4000))

    # CONFIRMING WE ARE A USER

    BANDWIDTH = 2048
    RECIEVING_HTML = False

    msg = s.recv(BANDWIDTH)
    print(msg.decode("utf-8"))
    # RETRIEVES THAT DATA
    while True:
        s.sendall("USER".encode())
        # ASKING FOR SOMETHING
        s.sendall(url.encode())
        a = s.recv(BANDWIDTH).decode()
        print(a)

        if a == "HTMLINCOMING":
            BANDWIDTH = 100000
            RECIEVING_HTML = True
            print("sdfjghsdfjg")



        else:
            BANDWIDTH = 2048

        if RECIEVING_HTML == True:
            a = s.recv(BANDWIDTH).decode()
            try:
                new_html_file = open("WEBSITE.html", "w")
                new_html_file.write(a)
                new_html_file.close()
                print("WROTE FILE")
            except:
                print("TRANSFER FAILED")

        RECIEVING_HTML = False
        print(a)
        break
