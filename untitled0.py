import socket

host = "nowyouseeme.binaryclash360.kctf.cloud"
port = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print("Connected to the server.")
    while True:
        data = s.recv(1024).decode()
        if not data:
            print("No more data. Exiting.")
            break
        print(data)
        if "flag" in data.lower():
            print("Flag received! Exiting.")
            break
