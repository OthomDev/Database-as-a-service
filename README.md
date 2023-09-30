# Database-as-a-service
<h1> Setting Up and Running the Application </h1>
<h2> Prerequisites: </h2>
Docker: This application requires Docker to be set up on your machine.<br>

Docker-Compose: If you're on Windows, Docker Compose will be automatically installed with Docker Desktop. For other operating systems, ensure you install Docker Compose separately.<br>

Postman provides a user-friendly interface to send requests to your API, making it a recommended tool for testing and interacting with your Database-as-a-Service application.<br>

<h2> Running the application </h2>
run: sudo docer-compose build
after the build run: docker-compose up

Endpoints: localhost:5000/register to register new user:

Ex: 
{
    "username": "new username",
    "password": "Password"
}

Endpoints: localhost:5000/store to store a sentence user:

Ex: 
{
    "username": "new username",
    "password": "Password"
    "sentence": "Write any data you want to store in this database"
}

Endpoints: localhost:5000/get to get the docuement of the user:

{
    "username": "new username",
    "password": "Password"
}

# Any request for Store or Get you lose one Coin (Tokens), By default any new user has 6 Tokens

