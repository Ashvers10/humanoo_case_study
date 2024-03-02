import pandas as pd
import duckdb
import os

cur_dir = os.getcwd()

conn = duckdb.connect(database= os.path.join(cur_dir,'humanoo_case_study.duckdb'))

# Define your SQL queries based on the dbt models
queries = {
    "Daily Average Steps": """SELECT * FROM public.daily_average_steps""",
    "Company User Activity": """SELECT * FROM public.company_user_activity""",
    "Top and Bottom 10 Users by Steps": """SELECT * FROM public.top_bottom_users"""
}

# Execute and display each query's result
for title, query in queries.items():
    print(f"{title}:")
    df = pd.read_sql_query(query, conn)
    print(df)
    print("\n")

# Close the connection
conn.close()
