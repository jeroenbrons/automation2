import socket
import sys
import hashlib
import subprocess,os
global antw
import logging

logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s - %(message)s',level=logging.INFO)
HOST = '' # Alle beschikbare interfaces
PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def checkpwd():
        conn.sendall(b'geef password')
        data = conn.recv(1024)
        data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
        hash=hashlib.md5(data.encode()).hexdigest()
        print(hash)
        if hash != '76d0dd90f9abe188e7f9027f6d24cf0b':
            conn.sendall(b"wachtwoord INCORRECT")
            conn.close()
            s.close()
        conn.sendall(b'Authenticatie correct')
        return True
antw=False
s.bind((HOST, PORT))
s.listen(10)
print('> Socket luistert op poort:', PORT)
conn, addr = s.accept()
while True:
    try:
        if '127.0.0.1' in addr[0]:
            logging.info('client allowed on' + addr[0])
        else:
            logging.info('client denied on' + addr[0])
            conn.close()
            s.close()
            continue
        print('> Verbonden met ' + addr[0] + ':' + str(addr[1]))
        # De server meldt zich aan de client
        conn.sendall(b'Welkom bij Jeroens socket: \n')
        # Wacht op input van de client en geef deze ook weer terug (echo service)
        #data = conn.recv(1024)
        #data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n

        if antw != True:
                antw= checkpwd()
        data = conn.recv(1024)
        data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
        if data=="stop":
            conn.sendall(b'going down')
            conn.close()
            s.close()
            antw=False
            break
        else:
            print('> Client data ontvangen:'+data+'<eindeData>')
            if data=="xterm":
                subprocess.call("xterm")
                logging.info('xterm started')
            elif data=="xfce4-notes":
                logging.info('xfce4-notes started')
                subprocess.call("xfce4-notes")
    except socket.error as msg:
        print(msg)
        sys.exit()

