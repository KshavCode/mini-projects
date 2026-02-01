# Salon Appointment Scheduler

This Python-based Salon Appointment Scheduler is a direct port of the Bash script originally designed for the FreeCodeCamp Relational Database certification. It manages service bookings by interacting with a PostgreSQL database to track customers, services, and appointments.

## 🛠 Features
* **Dynamic Service Menu**: Automatically fetches and displays available services from the database.
* **Customer Retention**: Recognizes returning customers by their phone number.
* **Automatic Registration**: Prompts new customers for their name and adds them to the database.
* **Sanitized Inputs**: Uses parameterized queries via `psycopg2` to prevent SQL injection.
* **Transaction Management**: Uses `commit()` to ensure data integrity during insertions.

## 📋 Prerequisites
* **Python 3.x**
* **PostgreSQL**
* **psycopg2 library**: Install via `pip install psycopg2-binary`

## 🗄 Database Schema
The script interacts with a PostgreSQL database named `salon` with the following tables:
* **customers**: `customer_id` (PK), `phone` (Unique), `name`.
* **services**: `service_id` (PK), `name`.
* **appointments**: `appointment_id` (PK), `customer_id` (FK), `service_id` (FK), `time`.



## 🚀 Usage
1. Update the `psycopg2.connect` parameters in `salon.py` to match your local PostgreSQL credentials.
2. Run the script:
   ```bash
   python3 salon.py