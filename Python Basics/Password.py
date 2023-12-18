def encrypt(password, shift):
    encrypted = ""
    for char in password:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                # Ensure wrapping around from 'z' to 'a'
                if shifted > ord('z'):
                    shifted = shifted - 26
            elif char.isupper():
                # Ensure wrapping around from 'Z' to 'A'
                if shifted > ord('Z'):
                    shifted = shifted - 26
            encrypted += chr(shifted)
        elif char.isdigit():
            shifted_digit = (int(char) + shift) % 10
            encrypted += str(shifted_digit)
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_password, shift):
    return encrypt(encrypted_password, -shift)

# Example usage
my_password = "Mainio2002"  # Replace with your password
shift = 3  # Number of places to shift

encrypted_password = encrypt(my_password, shift)
print("Encrypted Password:", encrypted_password)

decrypted_password = decrypt(encrypted_password, shift)
print("Decrypted Password:", decrypted_password)
