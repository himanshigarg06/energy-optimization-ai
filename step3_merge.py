import pandas as pd

# Load cleaned datasets
energy = pd.read_csv('cleaned_energy_availability.csv')
coal = pd.read_csv('cleaned_coal_plants.csv')
renewable = pd.read_csv('cleaned_renewable_potential.csv')

# Merge all datasets on State
df = energy.merge(coal, on='State', how='left')
df = df.merge(renewable, on='State', how='left')

# Fill missing values
df.fillna(0, inplace=True)

# Create features
df['Energy Deficit (MW)'] = df['Peak Demand (MW)'] - df['Peak Met (MW)']
df['Coal Dependency Ratio'] = df['Coal Requirement'] / (df['Peak Met (MW)'] + 1)

# Save final dataset
df.to_csv('final_dataset.csv', index=False)

print("Final dataset created!")
print(df.head())