import sqlite3
import pandas as pd

df = pd.read_csv("part_d_california.csv")

conn = sqlite3.connect("part_d.db")
df.to_sql("prescriptions", conn, if_exists="replace", index=False)
conn.close()

print(f"Loaded {len(df)} rows into part_d.db")