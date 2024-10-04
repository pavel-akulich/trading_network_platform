# Online platform of electronics retail network

[Russian](../README.md) | **English**

## Project description
The Online platform of electronics retail network is a backend part of an application created in the Python programming language using the Django REST framework.
The project includes a backend part responsible for data processing and business logic.

## Components of the project

The project consists of the following components:

1. **Application models**
    - Contains three models: `users`, `products`, `trading_networks`

2. **Admin panel**
    - Configured an administrative panel to manage application entities;
    - On the page with objects, objects have a link to the supplier;
    - Implemented filtering by city;
    - Implemented `admin action` to clear debts to supplier for selected objects.

3. **set of API views**
    - CRUD views for network and product objects;
    - A view to get information about all network objects;
    - View to get information about objects of a certain country (filter by name);
    - A view with statistics about objects whose debt exceeds the average debt of all objects;
    - A view to get all network objects where a certain product can be found (filter by product id);
    - A qr code with contact details of the network object is generated on API request and sent to the user's e-mail.

4. **Celery tasks**
    - Implemented a task that runs automatically every 3 hours and increase debt to a vendor by a random number from 5 to 500;
    - Implemented a task that runs automatically at 6:30 every day and decreases the debt owed to a supplier by a random number from 100 to 10,000;
    - Implemented a task that sends a QR code using email.


## Technologies
   - The project is developed in the `Python` programming language using `Django REST framework`
   - A third-party library `psycopg` is used to work with the `PostgreSQL` database
   - API documentation is connected in the project using `drf-yasg` library
   - The `poetry` tool is used to control the virtual environment
   - To interact with environment variables the `python-dotenv` library is used
   - The `celery` library is used to work with tasks
   - The `qrcode` library is used to generate QR codes.
   - `Docker` is used for easier project launching.

## Run the Project
### 1. Manual project start:
   - Clone the repository https://github.com/pavel-akulich/trading_network_platform
   - Install all dependencies from the `pyproject.toml` file
   - Create `.env` file in the root of the project and copy the contents of `.env.example` file into it, specifying the necessary values (database, email server, Celery settings).
   - Create a database and migrate to the database `python3 manage.py migrate`.
   - Run the `python3 manage.py loaddata trading_network_data.json` command to populate the database with test data
   - Run the server `python3 manage.py runserver`
   - Run the commands `celery -A config worker -l INFO` and `celery -A config beat -l INFO` to start Celery
   - The superuser will be accessible with the login `example@example.com` and password `password123`. Other users will have the same password.

### 2. Start a project using Docker:
   - Clone the repository https://github.com/pavel-akulich/trading_network_platform
   - Create `.env` file in the root of the project and copy the contents of `.env.example` file into it, specifying the necessary values (database, email server, Celery settings)
   - Use the `docker compose up --build` command to build and start all services
   - The database will be created automatically, then migrations will be applied and the database will be populated with test data from `trading_network_data.json`.
   - After successful completion of the previous step, the application will be available at http://127.0.0.1:8000/ or http://localhost:8000/
   - The superuser will be accessible with the login `example@example.com` and password `password123`. Other users will have the same password.

## API documentation
After the server is successfully launched locally, the API documentation will be available at the following addresses: http://127.0.0.1:8000/openapi/ or http://127.0.0.1:8000/openapi/redoc/

## Notes
   - The project can be further developed and extended for broader use
   - The environment variables required for the project to work can be viewed in the `.env.sample` file
   - All the necessary dependencies are in the files `pyproject.toml` and `poetry.lock`