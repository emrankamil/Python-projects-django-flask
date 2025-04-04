# Encryption/Decryption Tool

A Flask-based web application that implements OTP, AES, and 3DES encryption algorithms with user-friendly interfaces.

## Features

- One-Time Pad (OTP) encryption/decryption
- AES-256 encryption/decryption
- 3DES encryption/decryption
- Web-based interface with responsive design
- Client-side validation

## Prerequisites

- Python 3.8+
- pip package manager
- Git (for cloning the repository)

## Installation

### 1. Clone the repository:
   ```bash
   git clone https://github.com/emrankamil/Python-projects-django-flask
   cd Python-projects-django-flask/encryption
  ```

### 1. Set Up a Virtual Environment
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
flask run --debug
```

The application will be available at:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage Guide

1. Access the web interface in your browser.
2. Select an encryption method from the available options.
3. Enter your plaintext in the input field.
4. Provide a secret key (requirements vary by algorithm):
   - **OTP**: Key must be at least as long as the plaintext.
   - **AES**: Minimum 16 characters.
   - **3DES**: Minimum 16 characters.
5. Click **Encrypt/Decrypt** to see the results.

## Algorithms Implemented

| Algorithm | Key Requirements | Mode | Padding |
|-----------|-----------------|------|---------|
| **OTP**   | ≥ plaintext length | N/A | None |
| **AES**   | 16+ characters | ECB | PKCS#7 |
| **3DES**  | 16+ characters | ECB | Space |
