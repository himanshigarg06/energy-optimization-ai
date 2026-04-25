import pandas as pd

files = {
    'estimated_potential': 'estimated-potential.csv',
    'power_plants_coal': 'rs_session240_au83_1.2.csv',
    'energy_availability': 'MOP_energy_availability_1.csv',
    'product_consumption': 'productconsumption.csv'
}

for name, path in files.items():
    print(f"\n{'='*60}\nData Summary for {name} ({path})\n{'='*60}")
    try:
        df = pd.read_csv(path)
        print("Columns:\n", df.columns.tolist())
        print("\nSample (first 2 rows):")
        print(df.head(2).to_string())
        print("\nSummary Statistics:\n", df.describe())
        print("\nDuplicate Rows:", df.duplicated().sum())
        print("\nMissing values:\n", df.isnull().sum())
    except Exception as e:
        print(f"Error loading {path}: {e}")
