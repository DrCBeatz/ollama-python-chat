# Ollama Python Chat

A simple chat web app using Ollama and the dolphin-mistral:7b model. This project is suitable for running locally on a desktop or laptop, even without a GPU.

## Prerequisites

- Docker

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

`git clone https://github.com/yourusername/ollama-python-chat.git`

Then navigate to the project directory:

`cd ollama-python-chat`

### 2. Build and Run the Docker Containers

Build and run the Docker containers using Docker Compose:

`docker compose up -d --build`

### 3. Pull the Model

Pull the dolphin-mistral:7b model using the following command:

`docker compose exec ollama ollama pull dolphin-mistral:7b`

### 4. Access the Web App

Open your web browser and go to the following URL:

`http://localhost:5000/`

### 5. Stop the Containers

When you're done, stop the containers using:

`docker compose down`

### License

This project is licensed under the MIT License.