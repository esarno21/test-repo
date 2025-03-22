# Note: the module name is psycopg, not psycopg3
import psycopg
import pandas as pd
import os

# Connect to an existing database
with psycopg.connect("dbname=testdb user=postgres password=admin") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute(""" 
                BEGIN;
                DROP TABLE IF EXISTS test_table;
                CREATE TABLE test_table (
                user_id integer PRIMARY KEY,
                name_first text,
                name_last text)
            """)

        #get data for insert
        os.chdir(r'C:\Users\esarn\OneDrive\Desktop\coding\postgresql\testing\data_sets')
        df = pd.read_csv('testdb.user_test.csv')

        df.to_sql('test_table', con=conn)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO test_table (user_id) VALUES (1)"
        )

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test_table")
        cur.fetchone()
        # will return (1, 100, "abc'def")

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()