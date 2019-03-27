import socket
import select
import os

UDP_IP = "127.0.0.4"
IN_PORT = 9000
timeout = 5
save_path = 'D:/ProgjarF/ProgjarF/Tugas2/Client4/'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data1 = data[:5] + "Client4.jpg" 
    print("ini adalah "+data1)
    if data1:
        print "File name:", data1
        file_name = os.path.join(save_path, data1)

    f = open(file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data1, addr = sock.recvfrom(128000)
            f.write(data1)
        else:
            print "%s Finish!" % file_name
            f.close()
            break