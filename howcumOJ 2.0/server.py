__author__ = 'howcum'

# server2.py
import socket
from threading import Thread
#from SocketServer import ThreadingMixIn
import socketserver
import teacher_home
import os
import subprocess
import sqlite3

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

c_id=[]
s_id=[]

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print (" New thread started for " + ip + ":"+str(port))

    def run(self):
        filename='b.cpp'
        f = open(filename,'wb')
        print ('file opened')
        roll=[]
        problemnum=0
        while True:
            #print('receiving data...')
            data = self.sock.recv(BUFFER_SIZE)
            print('data=%s', (data))
            if not data:
                f.close()
                print ('file close()')
                break
            # write data to a file
            # i=0
            # for p in data:
            #     if i<10:
            #         print(data[p])
            #         roll+=str(p)
            #     else:
            #         #f.write(p)
            #         continue
            #     i+=1
            f.write(data)
            print(roll)
        command = ["g++.exe", "b.cpp" , "-o", "b.exe"]
        print (command)

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            os.system('"C:\\Users\\howcum\\PycharmProjects\\howcumOJ 2.0\\b.exe"')

            lines=[]
            with open('b.cpp') as f:
                lines=f.readline()
            f.close()
            #roll=[]
            roll=lines[2]+lines[3]+lines[4]+lines[5]+lines[6]+lines[7]+lines[8]+lines[9]+lines[10]
            print(roll)
            #lines[12] is the problem number
            flag=1
            f1=open('output'+lines[12]+'.txt')
            f2=open('out.txt')

            while f1.read()==True:
                if f1.read() != f2.read():
                    flag=0
                    break
                else:
                    continue

            f1.close()
            f2.close()
            self.conn = sqlite3.connect('mydatabase.db')
            problemnumber=int(lines[12])+1
            print(problemnumber)
            if flag==1:
                print("accepted "+roll + ' ' + str(problemnumber))
                self.c=self.conn.cursor()
                self.c.execute('SELECT * from Problems WHERE course_id= ? and session_id = ?',(c_id,s_id))
                self.now=self.c.fetchone()
                #print(self.now)
                i=0
                string=str(self.now[3])
                total=len(string)
                print(string,total)
                while i<=total-12:
                    if string[i]==roll[0] and string[i+1]==roll[1]and string[i+2]==roll[0+2]and string[i+3]==roll[0+3]and string[i+4]==roll[0+4]and string[i+5]==roll[0+5]and string[i+6]==roll[0+6]and string[i+7]==roll[0+7]and string[i+8]==roll[8]:
                        print("hello")
                        string=string[:8]+'10'+string[11:]
                        # new_list=list(string)
                        # new_list[i+9]='1'
                        # new_list[i+10]='0'
                        # ''.join(new_list)
                        break
                    else:
                        continue
                    i+=11
                # print(str(new_list))
                # string=str(new_list)
                self.c.execute('UPDATE Problems SET p'+str(problemnumber)+' = ? WHERE course_id= ? and session_id = ?',(string,c_id,s_id))

            else:
                print("wrong ans")

            #verdict="accpted"
            #self.sock.send(verdict.encode('ascii'))
        except:
            print("compilation error!!")
        self.conn.commit()
        self.conn.close()

def Main_server(CC_ID,SS_ID):
    global c_id
    global s_id
    c_id=CC_ID
    s_id=SS_ID
    teacher_home.call("hello")
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    threads = []

    while True:
        tcpsock.listen(5)
        print ("Waiting for incoming connections...")
        (conn, (ip,port)) = tcpsock.accept()
        print ('Got connection from ', (ip,port))
        newthread = ClientThread(ip,port,conn)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()


if __name__ == '__main__':
    Main_server("3022016","30220162")