from pathlib import Path
import psycopg2

# Database connection parameters
# conn_string = 'postgresql://postgres:admin@localhost:5433/test_db'
DB_PARAMS = {
    "dbname": "test_db",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5433",
}

# Path to CSV file
csv_file_path = Path("data_files/testdb__user_test.csv").resolve()

# Table name
table_name = "user_test"

# Drop / create table
sql_create_table = f" BEGIN; DROP TABLE IF EXISTS {table_name}; CREATE TABLE IF NOT EXISTS {table_name} (user_id int, name_first text, name_last text)"

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    # Open the CSV file
    with open(csv_file_path, "r") as f:
        # Skip the header row if necessary
        next(f)

        # Copy data from CSV to PostgreSQL table
        cur.execute(sql_create_table)
        cur.copy_from(f, table_name, sep=",", null="")

    # Commit changes
    conn.commit()
    print("CSV file uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
    conn.rollback()

finally:
    # Close connection
    cur.close()
    conn.close()
