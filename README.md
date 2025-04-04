
# Python Projects

This repository features two distinct projects developed using Python. 
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


# My Simple Portfolio Website - Project 2



## Project Overview

In this project, I built a basic Django application with a single app called "base." The main purpose of this website is to showcase my understanding of Django's core concepts and to provide a simple portfolio platform.

## Key Features

- **Server Creation**: I set up a Django server to host my website locally.
- **Homepage URL**: I created a URL mapping for the homepage and linked it to the main URL configuration of the project.

## Project Structure

The repository structure is organized around Django's standard layout, including the "base" app where the core functionality resides. You won't find any fancy features or complex functionalities in this project. It's all about getting to grips with the basics of Django.

Feel free to explore the code and see how I implemented Django's fundamental concepts in building this straightforward portfolio website. Whether you're a fellow learner or just curious about Django development, I hope this project serves as a helpful resource.
![djangoWeb](https://github.com/emrankamil/Django-projects/assets/128908090/2a17fca5-23ad-4e0d-bf15-980606bbec76)


#  To-Do App - Project 3
My second project is a To-Do App that handles simple Create, Update, and Delete operations using Django. This project taught me everything about models, databases, and a lot more about Django.

## Project Overview
In this project, I developed a Django-based To-Do application that allows users to manage their tasks effortlessly. It served as a practical exercise to deepen my understanding of Django's database capabilities and model-driven development.

## Key Features

- **Task Management**: Users can create, update, and delete tasks.
- **Database Integration**: The project extensively uses Django's models and database integration for storing task data.
User-Friendly Interface: The app provides an intuitive and user-friendly interface for task management.

# Project Structure
The repository structure adheres to Django's best practices, with a dedicated app for managing tasks. While the project primarily focuses on essential CRUD (Create, Read, Update, Delete) operations, it provides valuable insights into Django's powerful capabilities in building web applications.
![djangoToDoApp](https://github.com/emrankamil/Django-projects/assets/128908090/ac3b86de-b111-4974-b369-9d8724d9de7a)


