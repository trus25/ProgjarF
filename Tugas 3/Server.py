import sys
import socket
import os
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9001)
print >> sys.stderr, 'starting up on %s port %s' %server_address
sock.bind(server_address)

sock.listen(1)
namafile=["Server/bart1.png", "Server/bart2.png", "Server/bart3.png","Server/bart4.png","Server/bart5.png"]

def fungsi(conn):
    #conn = conndata[0]
    while True:
        req = conn.recv(32)
        if(req == '1'):
            for nama in namafile:
                conn.send(nama + "\n")
        elif(req == '2'):
            nama1 = conn.recv(1024)
            for nama in namafile:
                if (nama == nama1):
                    counter = '1'
                    break
                else :
                    counter = '0'
            conn.send(counter)
            if (counter == '1'):
                conn.send("START {}" . format(nama1))
                ukuran = os.stat(nama1).st_size
                fp = open(nama1,'rb')
                k = fp.read()
                terkirim=0
                for x in k:
                    conn.send(x)
                    terkirim = terkirim + 1
                    print "\r terkirim {} of {} " . format(terkirim,ukuran)
                fp.close()
                conn.send("DONE")
        elif(req == '3'):
            conn.send("READY")
            while True:
                data = conn.recv(1024)
                if(data[0:5]=="START"):
                    print data[6:]
                    nama1 = "Server/" + data[6:]
                    fp = open(nama1,'wb+')
                    ditulis=0
                elif(data=="DONE"):
                    fp.close()
                elif(data=="END"):
                    break
                else:
                    print "blok ", len(data), data[0:10]
                    fp.write(data)
            namafile.append(nama1)

while True:
    print "waiting for connection from client..."
    conn, addr = sock.accept()
    print >> sys.stderr, 'conn from', addr
    thread = Thread(target=fungsi, args=(conn, ))
    thread.start()