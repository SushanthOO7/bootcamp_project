import hashlib

print("Hashing Options : ")
print("1. SHA256")
print("2. SHA512")
print("3. SHA-1")

def sha256():
    txt = input("Enter your text to perform sha256 hashing: ")
    cip = hashlib.sha256(txt.encode())
    print(cip.hexdigest())

def sha512():
    txt2 = input("Enter your text to perform sha512 hashing: ")
    cip2 = hashlib.sha512(txt2.encode())
    print(cip2.hexdigest())

def sha1():
    txt3 = input("Enter your text to perform sha1 hashing : ")
    cip3 = hashlib.sha1(txt3.encode())
    print(cip3.hexdigest())

sha256()
sha512()
sha1()
