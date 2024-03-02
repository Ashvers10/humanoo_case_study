import duckdb


cursor = duckdb.connect(database='case_study.duckdb')


print(cursor.execute('select 42 as answer_to_life').fetchall())
