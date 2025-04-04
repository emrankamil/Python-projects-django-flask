from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import base64


# Load RSA Keys
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(open("public_key.pem", "rb").read())


def encrypt_rsa(plaintext):
    encrypted = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return base64.b64encode(encrypted).decode()


def decrypt_rsa(encrypted_text):
    try:
        decrypted = private_key.decrypt(
            base64.b64decode(encrypted_text),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return decrypted.decode()
    except Exception as e:
        return str(e)
