def modular_inverse(a, m):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0  # gcd, x, y such that ax + by = gcd
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        print("Modular inverse does not exist because a and m are not coprime.")
        return None
    else:
        return x % m  # Return the positive inverse

if __name__ == "__main__":
    a = int(input("Enter a: "))
    m = int(input("Enter m: "))
    
    inverse = modular_inverse(a, m)
    
    if inverse is not None:
        print(f"The modular inverse of {a} modulo {m} is: {inverse}")
