import base64


def encrypt_otp(plain_text, secret_key):
    """Encrypts the text using OTP with the given secret key."""
    if len(secret_key) < len(plain_text):
        return "Error: The key must be at least as long as the plain text."

    plain_text_bytes = plain_text.encode()
    key_bytes = secret_key.encode()

    encrypted_bytes = bytes(a ^ b for a, b in zip(plain_text_bytes, key_bytes))
    return base64.b64encode(encrypted_bytes).decode()


def decrypt_otp(cipher_text, secret_key):
    """Decrypts the text using OTP with the given secret key."""
    cipher_bytes = base64.b64decode(cipher_text.encode())

    key_bytes = secret_key.encode()

    decrypted_bytes = bytes(c ^ k for c, k in zip(cipher_bytes, key_bytes))

    return decrypted_bytes.decode()
