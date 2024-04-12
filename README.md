# Tamatem Plus

## Project Overview

This project is a web application developed using Django, a high-level Python web framework. It provides functionality for managing products and users, including user authentication and RESTful API endpoints.


## Installation

To install and run the application locally, follow these steps:

1. **Clone Repository**: Clone the repository to your local machine:

    ```bash
    git clone https://github.com/maram-mustafa/tamatem-plus-backend.git
    
    ```
2. **Install Dependencies**: Install project dependencies using Yarn:

    ```bash
    pip install -r requirements.txt
    ```
3. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Start Development Server**: Start the development server:

    ```bash
    python manage.py runserver
    ```

## Models

### `User`
### Custom User Model

The project uses a custom user model with email as the unique identifier. User passwords are securely encrypted.

- email: EmailField
- date_joined: DateTimeField
- last_login: DateTimeField
- is_active: BooleanField
- is_staff: BooleanField

### `Product`
- name: CharField
- description: TextField
- price: FloatField
- image: FileField

### Product Image Upload Path

Product images are stored in the `media` directory with a dynamically generated path based on the product's name and creation date.


## API Endpoints

### Products

- **GET /api/products**: Retrieve a list of all products.
- **POST /api/products**: Create a new product.
- **GET /api/products/{id}**: Retrieve details of a specific product.
- **PATCH /api/products/{id}**: Update details of a specific product.

### Users
- **POST /api/users**: Create a new user.








