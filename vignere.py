def vigenere_cipher(text, key, mode='encrypt'):
    result = ''
    key_length = len(key)
    key_as_int = [ord(k) - ord('A') for k in key.upper()]
    key_index = 0

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            reference = ord('A') if is_upper else ord('a')
            text_int = ord(char) - reference
            key_shift = key_as_int[key_index % key_length]
            if mode == 'decrypt':
                key_shift = -key_shift
            shifted = (text_int + key_shift) % 26
            result += chr(shifted + reference)
            key_index += 1
        else:
            result += char

    return result


if __name__ == "__main__":
    text = input("Enter text: ")
    key = input("Enter key: ")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

    ciphered_text = vigenere_cipher(text, key, mode)
    print(f"Ciphered text: {ciphered_text}")