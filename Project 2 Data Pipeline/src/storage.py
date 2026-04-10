from pathlib import Path
import pandas as pd
import sqlite3

DATA_DIR = Path("data/processed") # create a Path object for the directory where processed data will be stored
DATA_DIR.mkdir(parents=True, exist_ok=True)  # make a directory at this path; do not raise an error if the directory already exists
# The parents=True argument allows the creation of parent directories if they do not exist, ensuring that the entire path is created without errors.

def load_to_csv(df: pd.DataFrame, path: Path) -> None: # takes DataFrame and path, writes the df to that path as a CSV file
    df.to_csv(path, index=False) # index=False to avoid writing the index to the csv file

def load_to_sqlite(df: pd.DataFrame, db_path: Path) -> None: # takes DataFrame and database path, writes the df to that database
    conn = sqlite3.connect(db_path) # opens (or creates) the .db file and returns connection object
    df.to_sql("weather", conn, if_exists="append", index=False) # creates weather table; if_exists="append" to add new data to existing table
    conn.close() # without close, file may stay locked or have unflushed writes