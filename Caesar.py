def caesar_cipher(text, shift, mode='encrypt'):
    cipher_text = ''
    
    # Ensure shift is between 0–25
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            cipher = (ord(char) - base + shift) % 26 + base
            cipher_text += chr(cipher)
        else:
            # Leave non-alphabetic characters unchanged
            cipher_text += char
    
    return cipher_text

if __name__ == "__main__":
    text = input("Enter text: ")
    shift = int(input("Enter shift (0-25): "))
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    
    deciphered_text = caesar_cipher(text, shift, mode)
    print(f"deciphered_text: {deciphered_text}")