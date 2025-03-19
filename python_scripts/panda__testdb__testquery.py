from sqlalchemy import create_engine
import os
import psycopg2
import pandas as pd

#db connection config
conn_string = 'postgresql://postgres:admin@localhost:5433/test_db'
db = create_engine(conn_string)

#select query
query_sql = '''
select
    user_id
    , name_first
    , name_last
from public.user_test
'''

#query to dataframe
df = pd.read_sql(query_sql, db)

#filtered dataframe
print(df[df["name_first"].isin(["Eric"])])
