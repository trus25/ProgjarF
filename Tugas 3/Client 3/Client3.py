import sys
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9001)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
namafile=["bartc.jpg"]

try:
    print "1. List File 2. Request File 3. Send File 4. Close"
    while True:
        req = raw_input('>')
        sock.send(req)
        if(req == '1'):
            msg = sock.recv(1024)        
            print msg
        elif(req== '2'):
            namanya = raw_input('Masukan nama file > ')
            sock.send(namanya)
            counter = sock.recv(32)
            print counter
            if(counter == '1'):
                while True:
                    data = sock.recv(32)
                    if(data[0:5]=="START"):
                        print data[12:]
                        fp = open(data[12:],'wb+')
                        ditulis=0
                    elif(data[0:4]=="DONE"):
                        print data[0:5]
                        fp.close()
                        break
                    elif(data[0:3]=="END"):
                        print data[0:5]
                        break
                    else:
                        print "blok ", len(data), data[0:10]
                        fp.write(data)
            else :
                print "nama tidak ada"
            
        elif(req=='3'):
            nama = raw_input('Masukan nama file > ')
            sock.send("START {}" . format(nama))
            ukuran = os.stat(nama).st_size
            fp = open(nama,'rb')
            k = fp.read()
            terkirim=0
            for x in k:
                sock.send(x)
                terkirim = terkirim + 1
                print "\r terkirim {} of {} " . format(terkirim,ukuran)
            fp.close()
            sock.send("DONE")
            sock.send("END")
        elif(req=='4'):
            break
finally:
    print >> sys.stderr, 'closing socket'
    sock.close()