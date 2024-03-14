# FastAPI Code Generation API with Feedback Mechanism

This FastAPI application leverages OpenAI's GPT models to generate code snippets based on user descriptions and improves its outputs over time by incorporating user feedback, stored and managed through Redis. Designed for ease of use and scalability, it aims to streamline the development process by providing quick, relevant code suggestions that adapt to user preferences and feedback.

## Features

- **Dynamic Code Generation**: Generate tailored code snippets from user-provided descriptions.
- **Feedback-Driven Improvement**: Enhance future code generations by integrating user feedback into the model's prompt.
- **Docker Integration**: Simplified setup and deployment with Docker and Docker Compose for both the application and Redis database.

## Prerequisites

Before you begin, ensure you have installed:

- Docker and Docker Compose
- An OpenAI API key to access the GPT models

## Getting Started

### 1. Clone the Repository

Start by cloning the project to your local machine:

```sh
git clone https://github.com/yourgithub/fastapi-codegen.git
cd fastapi-codegen
```

### 2. Environment Setup
Create a .env file in the project root directory. Add your OpenAI API key and the Redis URL:
```
    OPENAI_API_KEY=your_openai_api_key
    REDIS_URL=redis://redis:6379
```
### 3. Build and Launch with Docker
Use Docker Compose to build and start the application:
```
    docker-compose up --build
```
The API will now be accessible at http://localhost:8000.


### Usage
Generate Code: Send a POST request to /generate-code/ with a JSON payload containing the description of the code you need.
Submit Feedback: Send a POST request to /submit-feedback/ with a JSON payload containing feedback for the previously generated code.

