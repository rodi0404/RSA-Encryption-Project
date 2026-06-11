#16 Bit RSA encryption
from sympy import randprime
import math


def calculatepq():
    p = randprime(2**15,2**16)
    q = randprime(2**15,2**16)
    n = p*q
    phi = (p-1)*(q-1)
    return n,phi

def chooseE(phi):
    e = 65537
    if math.gcd(e,phi) != 1:
        raise ValueError("e must be coprime to phi")
    return e

def calculateD(e,phi):
    d = pow(e,-1,phi)
    return d

def displayKeys(e,d,n,phi):
    print(f"Public Key (e,n): ({e}, {n})")
    print(f"Private Key (d,n): ({d}, {n})")
    print(f"Manual Verification: ({e}*{d}) % {phi} = {(e*d) %phi}")

def encrypt(message,e,n):
    message = list(message)
    enccharlist = []
    for char in message:
        charnr = ord(char)
        encrypted = pow(charnr,e,n)
        enccharlist.append(encrypted)
    return enccharlist

def decrypt(numberlist,d,n):
    decryptedchrlist= []
    for number in numberlist:
        decryptednr = pow(number,d,n)
        decrypted = chr(decryptednr)
        decryptedchrlist.append(decrypted)
    endstring = "".join(decryptedchrlist)
    return endstring


n,phi = calculatepq()
e = chooseE(phi)
d = calculateD(e,phi)
displayKeys(e,d,n,phi)
encryptedmessage = encrypt("Du Dummer Hund",e,n)
print(encryptedmessage)
message = decrypt(encryptedmessage,d,n)
print(message)