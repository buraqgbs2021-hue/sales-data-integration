import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURATION ---
# Replace 'password' with your real pgAdmin password
# Replace 'sales_db' with the name of the database you created in pgAdmin4
DB_SETTINGS = {
    "user": "postgres",
    "password": "0000",
    "host": "localhost",
    "port": "5432",
    "database": "your_practice_db"
}

def run_integration():
    try:
        # 1. Create the Connection String
        conn_str = f"postgresql://{DB_SETTINGS['user']}:{DB_SETTINGS['password']}@{DB_SETTINGS['host']}:{DB_SETTINGS['port']}/{DB_SETTINGS['database']}"
        engine = create_engine(conn_str)

        # 2. Load the CSV using Pandas (Anaconda standard)
        df = pd.read_csv('sales_data.csv')
        print("Successfully read CSV file.")

        # 3. Push data to PostgreSQL
        # This will create a table named 'cleaned_sales' automatically
        df.to_sql('cleaned_sales', engine, if_exists='replace', index=False)
        print("Professional Integration Complete: Data pushed to pgAdmin4!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_integration()