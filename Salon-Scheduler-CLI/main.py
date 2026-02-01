import psycopg2
import sys

def service_menu(conn, message=None):
    # Print the header/welcome message
    if message:
        print(f"\n{message}")
    else:
        print("\n~~~~~ MY SALON ~~~~~")
        print("\nWelcome to My Salon, how can I help you?\n")

    with conn.cursor() as cur:
        # Fetch available services
        cur.execute("SELECT service_id, name FROM services;")
        services = cur.fetchall()

        for service_id, name in services:
            print(f"{service_id}) {name}")

        try:
            service_id_selected = input().strip()
            # Check if the input is a valid ID
            cur.execute("SELECT name FROM services WHERE service_id = %s;", (service_id_selected,))
            service_name_row = cur.fetchone()
        except (psycopg2.Error, ValueError):
            service_name_row = None

        if not service_name_row:
            service_menu(conn, "I could not find that service. What would you like today?")
        else:
            service_name = service_name_row[0].strip()
            
            print("\nWhat's your phone number?")
            customer_phone = input().strip()

            cur.execute("SELECT customer_id, name FROM customers WHERE phone = %s;", (customer_phone,))
            customer_row = cur.fetchone()

            if not customer_row:
                print("\nI don't have a record for that phone number, what's your name?")
                customer_name = input().strip()
                cur.execute("INSERT INTO customers(name, phone) VALUES (%s, %s) RETURNING customer_id;", (customer_name, customer_phone))
                customer_id = cur.fetchone()[0]
                conn.commit()
            else:
                customer_id, customer_name = customer_row
                customer_name = customer_name.strip()

            print(f"\nWhat time would you like your {service_name}, {customer_name}?")
            service_time = input().strip()

            # Insert appointment
            cur.execute(
                "INSERT INTO appointments(customer_id, service_id, time) VALUES (%s, %s, %s);",
                (customer_id, service_id_selected, service_time)
            )
            conn.commit()

            print(f"\nI have put you down for a {service_name} at {service_time}, {customer_name}.")

def main():
    try:
        # Database connection details
        conn = psycopg2.connect(
            database="salon",
            user="freecodecamp",
            host="localhost",
            port="5432"
        )
        service_menu(conn)
        conn.close()
    except Exception as e:
        print(f"Error connecting to database: {e}")

if __name__ == "__main__":
    main()