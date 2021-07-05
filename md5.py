import hashlib


def md5():
    txt = input("Enter the text : ")
    cipher = hashlib.md5(txt.encode())
    print("The cipher text : ", cipher.hexdigest())


md5()
