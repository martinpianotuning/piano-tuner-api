# database.py

import sqlite3
import os
import libsql_client
from datetime import date

def get_db_connection():
    """
    Establishes a connection to the Turso cloud database using credentials
    stored in environment variables.
    """
    db_url = os.environ.get("TURSO_DB_URL")
    db_token = os.environ.get("TURSO_DB_AUTH_TOKEN")

    if not db_url or not db_token:
        raise ValueError("Turso database credentials not found in environment variables.")
        
    conn = libsql_client.create_client_sync(url=db_url, auth_token=db_token)
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    """
    Creates the 'customers' table in the Turso cloud database if it doesn't already exist.
    """
    try:
        conn = get_db_connection()
        print("Successfully connected to Turso for setup.")
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                address TEXT,
                area_city TEXT,
                postcode TEXT,
                piano_details TEXT,
                last_service_date TEXT,
                next_service_due TEXT,
                notes TEXT
            )
        """)
        # --- REMOVED --- conn.commit() is not needed with this library.
        conn.close()
        print("Database schema setup or verification complete on Turso.")
    except Exception as e:
        print(f"An error occurred during database setup: {e}")


def get_all_customers():
    """Fetches a list of all customers, sorted by name."""
    conn = get_db_connection()
    customers = conn.execute("SELECT id, first_name, last_name, area_city FROM customers ORDER BY last_name, first_name").fetchall()
    conn.close()
    return customers

def get_due_customers():
    """Fetches customers whose next service date is today or in the past."""
    conn = get_db_connection()
    today_str = date.today().strftime("%Y-%m-%d")
    query = "SELECT id, first_name, last_name, next_service_due FROM customers WHERE next_service_due != '' AND next_service_due <= ? ORDER BY next_service_due"
    customers = conn.execute(query, (today_str,)).fetchall()
    conn.close()
    return customers

def get_customer_details(customer_id):
    """Fetches all details for a single customer by their ID."""
    conn = get_db_connection()
    customer = conn.execute("SELECT * FROM customers WHERE id = ?", (customer_id,)).fetchone()
    conn.close()
    return customer

def search_customers_by_area_and_due_date(area_list):
    """Finds all customers in a list of areas, sorted by the soonest due date."""
    if not area_list: return []
    conn = get_db_connection()
    placeholders = ', '.join(['?'] * len(area_list))
    query = f"SELECT id, first_name, last_name, area_city, next_service_due FROM customers WHERE LOWER(area_city) IN ({placeholders}) ORDER BY next_service_due ASC"
    customers = conn.execute(query, area_list).fetchall()
    conn.close()
    return customers

def add_customer(data):
    """Adds a new customer to the database and returns the new ID."""
    conn = get_db_connection()
    query = """
        INSERT INTO customers (first_name, last_name, phone, email, address, 
                               area_city, postcode, piano_details, 
                               last_service_date, next_service_due, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    rs = conn.execute(query, (
        data['first_name'], data['last_name'], data['phone'], data['email'], data['address'],
        data['area_city'], data['postcode'], data['piano_details'], data['last_service_date'],
        data['next_service_due'], data['notes']
    ))
    # --- REMOVED --- conn.commit()
    new_id = rs.last_row_id
    conn.close()
    return new_id

def update_customer(customer_id, data):
    """Updates an existing customer's details in the database."""
    conn = get_db_connection()
    query = """
        UPDATE customers SET
            first_name = ?, last_name = ?, phone = ?, email = ?, address = ?,
            area_city = ?, postcode = ?, piano_details = ?, 
            last_service_date = ?, next_service_due = ?, notes = ?
        WHERE id = ?
    """
    conn.execute(query, (
        data['first_name'], data['last_name'], data['phone'], data['email'], data['address'],
        data['area_city'], data['postcode'], data['piano_details'], data['last_service_date'],
        data['next_service_due'], data['notes'], customer_id
    ))
    # --- REMOVED --- conn.commit()
    conn.close()

def delete_customer(customer_id):
    """Deletes a customer from the database by their ID."""
    conn = get_db_connection()
    conn.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    # --- REMOVED --- conn.commit()
    conn.close()