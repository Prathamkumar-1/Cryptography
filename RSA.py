def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
m = int(input("Enter the message (an integer less than p*q): "))

n = p * q
phi = (p - 1) * (q - 1)

# Step 1: Choose encryption key e
# We'll pick a small e like 3, 5, 7... until gcd(e, phi) == 1
e = 3
while gcd(e, phi) != 1:
    e += 2

# Step 2: Compute private key d
d = modinv(e, phi)

# Step 3: Encrypt and decrypt
c = pow(m, e, n)           # Encrypted message
m_decrypted = pow(c, d, n) # Decrypted message

print(f"\nPublic Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")
print(f"Encrypted Message: {c}")
print(f"Decrypted Message: {m_decrypted}")
