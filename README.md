# FastAPI E-commerce API

This repository contains a simple RESTful API built with FastAPI for managing products in an e-commerce application.

## Requirements

- Python 3.7+
- pip

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Run the `initialize_database()` function to create the SQLite database and insert sample data. You can do this by running the following command:

    ```bash
    python database_setup.py
    ```

## Running the API

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

- **GET /products**: Retrieve a list of all products.
- **GET /products/{product_id}**: Retrieve details of a specific product by its ID.
- **POST /products**: Create a new product with details like title, description, and price.
- **PUT /products/{product_id}**: Update an existing product based on its ID.
- **DELETE /products/{product_id}**: Delete a product by its ID.

## Usage

You can use tools like cURL, Postman, or a web browser to interact with the API endpoints.

Example:

- To retrieve all products:

    ```bash
    curl http://localhost:8000/products
    ```

- To create a new product:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title": "New Product", "description": "New Description", "price": 99.99}' http://localhost:8000/products
    ```

## Testing

To run unit tests, execute the following command:

```bash
pytest
```

---
