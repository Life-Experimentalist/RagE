# Getting Started with FastAPI Agentic Project

Welcome to the FastAPI Agentic Project! This guide will help you set up and run the application on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-agentic-project.git
   cd fastapi-agentic-project
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Copy the `.env.example` file to `.env` and update the values as needed.

   ```bash
   cp .env.example .env
   ```

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn app.main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Running with Docker

If you prefer to run the application using Docker, you can use the provided `docker-compose.yml` file.

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Start the application:

   ```bash
   docker-compose up
   ```

The application will be accessible at `http://localhost:8000`.

## Optional Add-ons

The project supports optional add-ons that can enhance its functionality. You can find these in the `addons` directory. To use them, simply import the desired plugins in your application code.

## Conclusion

You are now ready to start using the FastAPI Agentic Project! For more detailed information on the API endpoints, refer to the [API Reference](api_reference.md) and for architectural decisions, check the [Architecture](architecture.md) document. Happy coding!