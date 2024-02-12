# API Documentation

## Dealers

### 1. Create Dealer
- **Endpoint:** POST /dealers/
- **Description:** Create a new dealer.
- **Request Example:**
  ```json
  {
      "name": "ABC Motors",
      "location": "123 Main Street",
      "contact_info": "123-456-7890"
  }
  ```

### 2. Get Dealer by ID
- **Endpoint:** GET /dealers/{dealer_id}
- **Description:** Retrieve information about a specific dealer by ID.


### 3. Update Dealer
- **Endpoint:** PUT /dealers/{dealer_id}
- **Description:** Update information about a specific dealer.
- **Request Example:**
```json
    {
        "name": "Updated Motors",
        "location": "456 Updated Street",
        "contact_info": "987-654-3210"
    }
```

### 4. Delete Dealer
- **Endpoint:** DELETE /dealers/{dealer_id}
- **Description:** Delete a specific dealer by ID.

### 5. Get All Dealers

- **Endpoint:** GET /dealers/
- **Description:** Retrieve a list of all dealers.

## Cars

### 1. Create Car
- **Endpoint:** POST /cars/
- **Description:** Create a new car.
- **Request Example:**
  ```json
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2022,
        "color": "Silver",
        "vin": "123456789",
        "price": 25000.00,
        "dealer_id": 1
    }
  ```
### 2. Get Car by ID
- **Endpoint:** GET /cars/{car_id}
- **Description:** Retrieve information about a specific car by ID.

### 3. Update Car
- **Endpoint:** PUT /cars/{car_id}
- **Description:** Update information about a specific car.
- **Request Example:**
```json
    {
        "make": "Updated Toyota",
        "model": "Updated Camry",
        "year": 2023,
        "color": "Blue",
        "vin": "987654321",
        "price": 27000.00
    }
```
### 4. Delete Car
- **Endpoint:** DELETE /cars/{car_id}
- **Description:** Delete a specific car by ID.

### 5. Get All Cars

- **Endpoint:** GET /cars/
- **Description:** Retrieve a list of all cars.

## Customers

### 1. Create Customer
- **Endpoint:** POST /customers/
- **Description:** Create a new customer.
- **Request Example:**
  ```json
    {
        "first_name": "John",
        "last_name": "Doe",
        "contact_info": "555-1234",
        "address": "456 Oak Street"
    }
  ```
### 2. Get Customer by ID
- **Endpoint:** GET /customers/{customer_id}
- **Description:** Retrieve information about a specific customer by ID.

### 3. Update Customer
- **Endpoint:** PUT /customers/{customer_id}
- **Description:** Update information about a specific customer.
- **Request Example:**
```json
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "contact_info": "555-5678",
        "address": "789 Maple Street"
    }
```
### 4. Delete Customer
- **Endpoint:** DELETE /customers/{customer_id}
- **Description:** Delete a specific customer by ID.

### 5. Get All Customers

- **Endpoint:** GET /customers/
- **Description:** Retrieve a list of all customers.

## Sales

### 1. Create Sale
- **Endpoint:** POST /sales/
- **Description:** Create a new sale.
- **Request Example:**
  ```json
    {
        "sale_date": "2024-02-10",
        "sale_amount": 30000.00,
        "payment_method": "Credit Card",
        "dealer_id": 1,
        "car_id": 1,
        "customer_id": 1
    }
  ```
### 2. Get Sale by ID
- **Endpoint:** GET /sales/{sale_id}
- **Description:** Retrieve information about a specific sale by ID.

### 3. Update Sale
- **Endpoint:** PUT /sales/{sale_id}
- **Description:** Update information about a specific sale.
- **Request Example:**
```json
    {
        "sale_date": "2024-02-15",
        "sale_amount": 32000.00,
        "payment_method": "Cash"
    }
```
### 4. Delete Sale
- **Endpoint:** DELETE /sales/{sale_id}
- **Description:** Delete a specific sale by ID.

### 5. Get All Sales

- **Endpoint:** GET /sales/
- **Description:** Retrieve a list of all sales.

## Python Version
- Python 3.8.10

## Usage

- Install dependencies using **pip install -r requirements.txt**
- Run the FastAPI application using **uvicorn main:app --reload**
- Access the Swagger documentation at **http://127.0.0.1:8000/docs** for interactive API testing.
- You can also use postman collection for testing API requests


## Why FastAPI?

- **High Performance:** FastAPI offers high-performance capabilities, ensuring efficient handling of API requests and responses.
- **Easy Development:** FastAPI's intuitive interface and automatic API documentation generation simplify the development process, enabling faster iteration.
- **Built-in Validation:** FastAPI leverages Pydantic for data validation, ensuring the integrity of data exchanged between clients and the API endpoints.
- **Automatic API Documentation:** FastAPI automatically generates interactive API documentation, reducing the need for manual documentation efforts and keeping documentation up-to-date with the codebase.
- **Type Safety:** FastAPI embraces Python type hints, enhancing code quality and maintainability by enabling static type checking and early error detection.

## Why SQLite?

- **Lightweight Nature:** SQLite is lightweight and easy to set up, making it suitable for small to medium-sized applications without the need for a separate database server.
- **Portability:** SQLite databases are self-contained within a single file, making them highly portable and easy to distribute across different systems.
- **Relational Database Capabilities:** Despite its lightweight nature, SQLite provides robust relational database capabilities, supporting SQL queries, indexes, views, triggers, and foreign key constraints.
- **Transaction Support:** SQLite supports ACID transactions, ensuring data integrity and reliability.
- **Compatibility:** SQLite is compatible with most programming languages and platforms, making it a versatile choice for a wide range of applications.
