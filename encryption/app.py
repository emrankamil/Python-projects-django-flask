from flask import Flask, render_template, request, jsonify

from aes_logics import decrypt_aes, encrypt_aes
from des3_logics import decrypt_3des, encrypt_3des
from otp_logics import decrypt_otp, encrypt_otp


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/otp")
def otp():
    return render_template("otp.html")


@app.route("/aes")
def aes():
    return render_template("aes.html")


@app.route("/3des")
def des():
    return render_template("3des.html")


# OTP routes
@app.route("/otp_encrypt", methods=["POST"])
def otp_encrypt():
    data = request.get_json()
    plain_text = data.get("plain_text", "")
    secret_key = data.get("secret_key", "")

    encrypted_text = encrypt_otp(plain_text, secret_key)
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/otp_decrypt", methods=["POST"])
def otp_decrypt():
    data = request.get_json()
    encrypted_text = data.get("encrypted_text", "")
    secret_key = data.get("secret_key", "")

    decrypted_text = decrypt_otp(encrypted_text, secret_key)
    return jsonify({"decrypted_text": decrypted_text})


# AES routes
@app.route("/aes_encrypt", methods=["POST"])
def aes_encrypt():
    data = request.get_json()
    plain_text = data.get("plain_text", "")
    secret_key = data.get("secret_key", "")

    encrypted_text = encrypt_aes(plain_text, secret_key)
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/aes_decrypt", methods=["POST"])
def aes_decrypt():
    data = request.get_json()
    encrypted_text = data.get("encrypted_text", "")
    secret_key = data.get("secret_key", "")

    decrypted_text = decrypt_aes(encrypted_text, secret_key)
    return jsonify({"decrypted_text": decrypted_text})


# 3DES routes
@app.route("/3des_encrypt", methods=["POST"])
def des3_encrypt():
    data = request.get_json()
    plain_text = data.get("plain_text", "")
    secret_key = data.get("secret_key", "")

    encrypted_text = encrypt_3des(plain_text, secret_key)
    print(f"Encrypted text: {encrypted_text}")
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/3des_decrypt", methods=["POST"])
def des3_decrypt():
    data = request.get_json()
    encrypted_text = data.get("encrypted_text", "")
    secret_key = data.get("secret_key", "")

    decrypted_text = decrypt_3des(encrypted_text, secret_key)
    return jsonify({"decrypted_text": decrypted_text})


if __name__ == "__main__":
    app.run(debug=True)
