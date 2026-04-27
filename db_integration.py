import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURATION ---
DB_SETTINGS = {
    "user": "postgres",
    "password": "YOUR_PASSWORD_HERE", # Remember to use your real password!
    "host": "localhost",
    "port": "5432",
    "database": "your_practice_db"
}

def run_integration():
    try:
        # 1. Create the Connection String
        conn_str = f"postgresql://{DB_SETTINGS['user']}:{DB_SETTINGS['password']}@{DB_SETTINGS['host']}:{DB_SETTINGS['port']}/{DB_SETTINGS['database']}"
        engine = create_engine(conn_str)

        # 2. Load the CSV
        df = pd.read_csv('sales_data.csv')
        print("CSV loaded successfully.")

        # --- NEW STEP: DATA TRANSFORMATION ---
        # We are creating a new column by multiplying units and price
        df['total_revenue'] = df['units_sold'] * df['unit_price']
        
        # We can also add a 'tax' column (e.g., 10%)
        df['tax_amount'] = df['total_revenue'] * 0.10
        
        print("Calculations complete: Added Revenue and Tax columns.")

        # 3. Push the ENHANCED data to PostgreSQL
        df.to_sql('enhanced_sales', engine, if_exists='replace', index=False)
        print("Professional Integration Complete: Enhanced data pushed to pgAdmin4!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_integration()