### What is this repo for?
This repository is the base for case Study at Humanoo, for Analytics Engineer position.
The purpose of it is to test the knowledge of: Python, SQL, dbt

### Setup / Stack

Please use **only** these "tools":
- **Python** 3.9 or higher.
- **dbt-core** 1.5.x or higher
- **duckdb** 0.9.x
# User Steps Analysis with dbt and DuckDB

## Overview

This project utilizes dbt (data build tool) and DuckDB to perform transformative analytics on user steps data. Our goal is to derive meaningful insights into user activity, segmented by individual performance and company affiliation. This project encompasses the entire workflow from data loading to transformation and analysis, leveraging dbt's powerful modeling capabilities alongside DuckDB's lightweight and efficient data processing.

## Project Structure

The project is structured as follows:

- `models/`: Contains dbt models for transforming raw data into analytical insights.
  - `/staging`: Staging models for initial data cleaning and preparation.
  - `/analysis`: Analytical models that provide the basis for our queries and insights.
- `data/`: Directory for CSV files containing raw data (not included in the repo for privacy reasons).


## Key Insights

The project aims to answer three primary questions:

1. **Daily Average Steps**: What is the daily average number of steps taken by all users across all days?
2. **Company Activity Insights**: How does user activity distribute across companies, and what percentage of users within each company are actively contributing steps data?
3. **Top and Bottom Performers**: Who are the top 10 and bottom 10 users based on the highest and least number of steps recorded in a single day?

## Setup Instructions

### Prerequisites

- Python 3.9+
- dbt-core and dbt-duckdb
- Pandas

### Installation

1. **Install Python Dependencies**:

   ```bash
   pip install dbt-duckdb pandas
   ```

2. **Initialize dbt Project**:

    Navigate to your project directory and run:

   ```bash
    dbt init humanoo_dbt
   ```  

3. **Configure profiles.yml**:

    Ensure your profiles.yml (located in ~/.dbt/) is correctly set up to use DuckDB:

    ```
    humanoo_dbt:
  target: dev
  outputs:
    dev:
      type: duckdb
      threads: 1
      database: '/path/to/your/duckdb_file.duckdb'
    ```

4. **Load Data into DuckDB**:

    Use the provided Python script (load_data.py) to load your CSV data into DuckDB using below cmd

    ```
    python load_data.py
    ```

5. **Running dbt Models**:

    Navigate to your dbt project directory and run:

    ```
    cd humanoo_dbt
    dbt run
    ```

6. **View the result**:

    Use the provided Python script (dbt_analysis_result.py) to view the result using below cmd

    ```
    cd ..
    python dbt_analysis_result.py
    ```


During this Case Study you would need DuckDB as your DB Engine.
You could install only this package: "dbt-duckdb"
, which will install: dbt-code, duckdb

You can test if you installed DuckDB properly using "duckdb_test.py"


### Tasks
1. Use files inside "source_files" directory as foundation or source for your dbt models, with this data model
   - **users**:
     - user_id - Unique Identifier of a User
     - user_name - Nickname of a User
     - company_id - Unique Identifier of a Company
     - company_name - Company Name
     - company_size - Number of employees
   - **steps_data**:
     - **activity_date** - Date of activity (i.e. when the steps were tracked)
     - **user_id** - Unique Identifier of a User
     - **steps** - How many steps were tracked
2. Design your dbt models, so they could be a foundation for you to answer the question below
3. Write these Queries **with SQL** and **show** the result (either with Pandas or any other plotting package):
    - Show the daily average number of steps for all the users, accross all days
            An example of the expected outcome: 10.000 (i.e. just a single number)
    - Show per "Company Name" amount of users and calculate % of how many users have steps data
    - Show the top 10 and bottom 10 users with the most (and least) steps collect in any day
            Output shoudl be for both top & bottom: "User Name" and "Number of Steps"

### How to share the result?
1. Clone (don't fork) this repository
2. Do the necessary changes
3. Don't forget to commit/push them
4. Share your cloned repo URL
5. P.S. it's ok to commit/push after you submitted your work, better later then never
