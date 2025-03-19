import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# Database connection URL
db_url = 'postgresql://postgres:admin@localhost:5433/test_db'

# Read CSV into a DataFrame
df = pd.read_csv(Path("data_files/testdb__user_test.csv").resolve())

# Table name
tablename = "user_test"

# Create a database engine
engine = create_engine(db_url)

# Upload DataFrame to PostgreSQL
df.to_sql("user_test", engine, if_exists="append", index=False)
print("CSV uploaded successfully!")
