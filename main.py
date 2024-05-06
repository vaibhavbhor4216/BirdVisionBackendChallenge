import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Creating the database and inserting sample data
def initialize_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        description TEXT,
                        price REAL
                    )''')
    cursor.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)", ("Cloths", "dark", 10.99))
    cursor.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)", ("Footwear", "branded", 20.99))
    cursor.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)", ("Jewellery", "golden", 30.99))
    conn.commit()
    conn.close()

initialize_database()

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Get all products
@app.get("/products")
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

#Get a specific product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

#Create a new product
@app.post("/products")
def create_product(title: str, description: str, price: float):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    conn.commit()
    new_product_id = cursor.lastrowid
    conn.close()
    return {"id": new_product_id, "title": title, "description": description, "price": price}

#Update an existing product by ID
@app.put("/products/{product_id}")
def update_product(product_id: int, title: str, description: str, price: float):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET title = ?, description = ?, price = ? WHERE id = ?", (title, description, price, product_id))
    conn.commit()
    conn.close()
    return {"message": "Product updated successfully"}

#Delete a product by ID
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    return {"message": "Product deleted successfully"}
