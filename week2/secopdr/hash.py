import hashlib
def passwdcheck():
    with open("passwd", "r") as storedPWD:
        data = hashlib.sha224(input("newpwd: ").encode()).hexdigest().encode()
        hash = storedPWD.read().encode()
        if data==hash:
            print("password correct")
            return True
        else:
            print("password incorrect")
            return False
passwdcheck()
