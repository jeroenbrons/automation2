import socket
import sys
import hashlib
with open("passwd", "w") as storedPWD:
    data = input("newpwd: ")
    hash = hashlib.md5(data.encode()).hexdigest()
    storedPWD.write(hash)
