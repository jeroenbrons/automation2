import socket
import sys
import hashlib
import subprocess
HOST = '' # Alle beschikbare interfaces
PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def checkpwd():
    with open("passwd", "r") as storedPWD:
        hash=hashlib.md5(data.encode()).hexdigest()
        if hash != storedPWD:
            conn.sendall(b"wachtwoord INCORRECT")
            conn.close()
            s.close()

while True:
    try:
        s.bind((HOST, PORT))
        s.listen(10)
        print('> Socket luistert op poort:',PORT)
        # Wacht op connecties (blocking)
        conn, addr = s.accept()
        # Er is een client verbonden met de server
        print('> Verbonden met ' + addr[0] + ':' + str(addr[1]))
        # De server meldt zich aan de client
        conn.sendall(b'WelkomOpMijnServer, vertel me iets, dan zeg ik hetzelfde terug:\n')
        # Wacht op input van de client en geef deze ook weer terug (echo service)
        data = conn.recv(1024)
        data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
        checkpwd()
        if data=="stop":
            conn.sendall(b'going down')
            conn.close()
            s.close()
            break
        else:
            print('> Client data ontvangen:'+data+'<eindeData>')
            conn.sendall(b"jeStuurdeMijDezeData:"+data.encode())
            conn.sendall(b'\n')
            # Verbreek de verbinding en sluit de socket
            conn.close()
            s.close()
    except socket.error as msg:
        print(msg)
        sys.exit()

