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

### 2. Create a .env File

Create a .env file in the root of the project directory and add the following line to specify the LLM model name:

`MODEL_NAME=llama3.1:8b`

You can change `llama3.1:8b` to any other model you want to use.


### 3. Build and Run the Docker Containers

Build and run the Docker containers using Docker Compose:

`docker compose up -d --build`

### 4. Pull the Model

Pull the llama3.1:8b model using the following command:

`docker compose exec ollama ollama pull llama3.1:8b`

### 5. Access the Web App

Open your web browser and go to the following URL:

`http://localhost:5000/`

### 6. Stop the Containers

When you're done, stop the containers using:

`docker compose down`

### License

This project is licensed under the MIT License.