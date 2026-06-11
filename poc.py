p = 61
q = 53
n = p*q #3233
phi = (p-1)*(q-1)
e = 17 #65537 - Teilerfremd zu phi - Public Key
d = 2753 # Erweiterter Euklidischer Algorithmus - Private Key


if (e*d)%3120 == 1:
    print("Gutes d")

chrzahl = ord("A")
enc = pow(chrzahl,e)%n
print(enc)

dec = pow(enc,d)%n
print(dec)