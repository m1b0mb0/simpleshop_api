# SimpleShop RESTful API 🛒

A robust and scalable backend API for an e-commerce platform. This project handles user authentication, product catalog management, shopping cart logic, secure checkout, and asynchronous order processing.

## Technologies
* `Python`
* `Django`
* `Django REST Framework`
* `PostgreSQL`
* `JSON Web Tokens`
* `Celery`
* `Redis`
* `Docker`
* `drf-spectacular`

## Features
* Secure user registration and JWT-based authentication.
* Hierarchical product catalog with filtering, searching, and pagination.
* Database-backed shopping cart with strictly isolated user access.
* Checkout system utilizing atomic database transactions to ensure data integrity.
* Asynchronous email notifications for order confirmations via Celery.

## Process
I started developing this API with the core database models for products and categories. I used generics to maintain explicit control over HTTP methods and routing. After securing the endpoints with JWT authentication, I implemented the business logic for a database-backed shopping cart. I designed the checkout process using Django’s atomic transactions to ensure safe order creation and proper cart clearing. Finally, I integrated Docker, Redis, and Celery to handle background sending  of order confirmation emails without blocking the main API thread.

## Running the Project
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Start infrastructure services (PostgreSQL & Redis): `docker-compose up -d`
4. Apply database migrations: `python manage.py migrate`
5. Start the Django development server: `python manage.py runserver`
6. Start the Celery worker in a separate terminal: `celery -A config worker -l info --pool=solo`
7. Open `http://127.0.0.1:8000/api/docs/swagger-ui/` in your browser
