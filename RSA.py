def isPrime(a):
    if a == 2:
        return True
    elif (a < 2) or ((a % 2) == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True

def generateKeys():
    print("Entrer les valeurs de 'P' et 'Q' :")
    p = int(input("Entrer un nombre premier pour 'P': "))
    q = int(input("Entrer un nombre premier pour 'Q': "))
    
    p_prime = isPrime(p)
    q_prime = isPrime(q)
    
    while (p_prime == False or q_prime == False):
        print("Vérifiez que p et q se sont deux nombres premiers!!!")
        p = int(input("Enter un nombre premier pour p : "))
        q = int(input("Enter un nombre premier pour q : "))
        p_prime = isPrime(p)
        q_prime = isPrime(q)
    N = p * q
    phiN = (p - 1) * (q - 1)
    print(f"Phi(N): {phiN}")
    print("Entrer la valeur de 'e':")
    e = int(input("'e' Doit être un nombre premier avec Phi(N)  &  1 < e < phiN: "))
    
    while (isCoPrime(e, phiN) == False) or (e > phiN):
        print("'E' Doit être un nombre premier avec Phi(N)  &  1 < e < phiN: ")
        e = int(input("Entrer la valeur de 'e':"))
    d = modularInv(e, phiN)
    return e, d, N, phiN

def isCoPrime(p, q):
    return gcd(p, q) == 1

def gcd(p, q):
    while q:
        p, q = q, p % q
    return p

def egcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    # return gcd, x, y
    return old_r, old_s, old_t

def modularInv(a, b):
    gcd, x, y = egcd(a, b)
    if x < 0:
        x += b
    return x

def encrypt(e, N, msg):
    cipher = ""
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "
    return cipher

def decrypt(d, N, cipher):
    msg = ""
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))
    return msg

def main():
    e, d, N, phiN = generateKeys()
    msg = input("Le message à Crypter ou à Décrypter : ")
    print("Votre message est : ", msg)
    print(f"e : {e}")
    print(f"d : {d}")
    print(f"N : {N}")
    print(f"Phi(N) : {phiN}")
    print(f"La clé publique : ({N},{e})")
    print(f"La clé privé : ({d},{N})")
    choose = input("Entrer '1' pour Crypter et '2' pour Décrypter : ")
    if choose == '1':
        enc = encrypt(e, N, msg)
        print("Le message Crypté est : ", enc)
    elif choose == '2':
        dec = decrypt(d, N, msg)
        print("Le message Décrypté est : ", dec)
    else:
        print("Votre choix n'est pas correcte.")

    print("Merci pour votre confiance en RSA. A bientot!")
main()
