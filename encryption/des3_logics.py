from Crypto.Cipher import DES3
import base64
import hashlib


def pad(text):
    """Pads the text to be a multiple of 8 bytes for 3DES."""
    while len(text) % 8 != 0:
        text += " "
    return text


def get_3des_key(secret_key):
    """Ensure the key is exactly 24 bytes long for 3DES."""
    hashed_key = hashlib.md5(secret_key.encode()).digest()  # Generate a 16-byte hash
    return hashed_key + hashed_key[:8]  # Extend to 24 bytes


def encrypt_3des(plain_text, secret_key):
    """Encrypts text using 3DES with the given secret key."""
    if len(secret_key) < 16:
        return "Error: Secret key must be at least 16 characters."

    key = get_3des_key(secret_key)
    cipher = DES3.new(key, DES3.MODE_ECB)  # Using ECB mode

    padded_text = pad(plain_text)
    encrypted_text = cipher.encrypt(padded_text.encode("utf-8"))

    return base64.b64encode(encrypted_text).decode("utf-8")


def decrypt_3des(encrypted_text, secret_key):
    """Decrypts 3DES-encrypted text with the given secret key."""
    if len(secret_key) < 16:
        return "Error: Secret key must be at least 16 characters."

    key = get_3des_key(secret_key)
    encrypted_bytes = base64.b64decode(encrypted_text.encode("utf-8"))

    cipher = DES3.new(key, DES3.MODE_ECB)

    decrypted_text = cipher.decrypt(encrypted_bytes).decode("utf-8").rstrip(" ")

    return decrypted_text
