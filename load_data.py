import os
import duckdb
import pandas as pd

# Get the current directory where this script is located
current_directory = os.getcwd()

# Construct the full paths to the CSV files
users_csv_path = os.path.join(current_directory, 'source_files', 'users.csv')
steps_csv_path = os.path.join(current_directory, 'source_files', 'steps.csv')

steps_df = pd.read_csv(steps_csv_path)

# Convert 'activity_date' to datetime, setting errors='coerce' to replace invalid dates with NaT
steps_df['activity_date'] = pd.to_datetime(steps_df['activity_date'], errors='coerce')

# Calculate the median of the valid dates
median_date = steps_df['activity_date'].median()

# Replace NaT (Not a Time) values with the median date
steps_df['activity_date'].fillna(median_date, inplace=True)

# Save the modified data back to the original CSV file
steps_df.to_csv(steps_csv_path, index=False)

# Connect to DuckDB
# Replace ':memory:' with 'path/to/your/humanoo_case_study.duckdb' to make it persistent
conn = duckdb.connect(database='humanoo_case_study.duckdb', read_only=False)

# Create tables and import data from CSV for 'users'
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER,
    user_name VARCHAR,
    company_id INTEGER,
    company_name VARCHAR,
    company_size VARCHAR
)
""")

conn.execute(f"""
COPY users FROM '{users_csv_path}' WITH (HEADER)
""")

# Create tables and import data from CSV for 'steps_data'
conn.execute("""
CREATE TABLE IF NOT EXISTS steps_data (
    activity_date DATE,
    user_id INTEGER,
    steps INTEGER
)
""")

conn.execute(f"""
COPY steps_data FROM '{steps_csv_path}' WITH (HEADER, DELIMITER ',', QUOTE '"', ESCAPE '"')
""")

# Verify loading by querying
print("Sample data from 'users':")
print(conn.execute("SELECT * FROM users LIMIT 5").fetchall())

print("\nSample data from 'steps_data':")
print(conn.execute("SELECT * FROM steps_data LIMIT 5").fetchall())

# Close the connection when done
conn.close()
