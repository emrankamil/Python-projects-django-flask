from Crypto.Cipher import AES
import base64


def pad(text):
    """Pads the text to be AES block size (16 bytes)."""
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)


def encrypt_aes(plain_text, secret_key):
    """Encrypts the text using AES with the given secret key."""
    if len(secret_key) < 16:
        return "Error: Secret key must be at least 16 characters."

    # Ensure the key is exactly 16, 24, or 32 bytes long (AES requirement)
    secret_key = secret_key[:32].ljust(32)

    cipher = AES.new(secret_key.encode("utf-8"), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode("utf-8"))
    return base64.b64encode(encrypted_text).decode("utf-8")


def decrypt_aes(encrypted_text, secret_key):
    """Decrypts the text using AES with the given secret key."""
    if len(secret_key) < 16:
        return "Error: Secret key must be at least 16 characters."

    # Ensure the key is exactly 16, 24, or 32 bytes long (AES requirement)
    secret_key = secret_key[:32].ljust(32)

    cipher = AES.new(secret_key.encode("utf-8"), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8")
    return decrypted_text.rstrip(decrypted_text[-1])
