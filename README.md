# Vigenere Cipher App

This is a Django web application for encrypting and decrypting messages using the Vigenere Cipher.

## Getting Started

### Prerequisites
- Docker must be installed on your system.

### Starting the Application
1. Clone this repository to your local machine.
2. Navigate to the project directory:
	cd vigenere_project
3. Build the Docker image:
	docker build -t my-django-vigenere-app .
4. Run the Docker container:
	docker run -p 8000:8000 my-django-vigenere-app

The application will be accessible at http://localhost:8000/.

### Stopping the Application
- To stop the application, press `Ctrl + C` in the terminal where the Docker container is running.

## Author
- Sujeet Madihalli
