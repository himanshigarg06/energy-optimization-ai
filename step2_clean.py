import pandas as pd
import numpy as np

# 1. Clean MOP_energy_availability_1.csv
print("Cleaning Energy Availability Dataset...")
mop_df = pd.read_csv('MOP_energy_availability_1.csv')

# Standardize State names
mop_df['State'] = mop_df['State'].str.strip().str.title()
# Keep relevant columns (focusing on MW for consistency)
mop_relevant = mop_df[['Month', 'State', 'Peak Demand (MW)', 'Peak Met (MW)', 'Demand not met (MW)']].copy()

# Note: The dataset contains multiple months. Let's keep the maximum or average? 
# For now, we just clean the strings. If there are commas in numbers, let's remove them.
for col in ['Peak Demand (MW)', 'Peak Met (MW)', 'Demand not met (MW)']:
    if mop_relevant[col].dtype == object:
        mop_relevant[col] = pd.to_numeric(mop_relevant[col].str.replace(',', ''), errors='coerce')

# Drop any potential NaN after coercion
mop_relevant.dropna(inplace=True)
# Aggregate state-wise (IMPORTANT)
mop_grouped = mop_relevant.groupby('State').agg({
    'Peak Demand (MW)': 'mean',
    'Peak Met (MW)': 'mean',
    'Demand not met (MW)': 'mean'
}).reset_index()

mop_grouped.to_csv('cleaned_energy_availability.csv', index=False)
print(f"Saved cleaned_energy_availability.csv. Shape: {mop_grouped.shape}")
#print(f"Saved cleaned_energy_availability.csv. Shape: {mop_relevant.shape}")

# 2. Clean rs_session240_au83_1.2.csv (Coal Power Plants)
print("\nCleaning Coal Power Plants Dataset...")
coal_df = pd.read_csv('rs_session240_au83_1.2.csv')

# Remove Sub Total and Total rows
coal_df = coal_df[~coal_df['Sr. No.'].isin(['Sub Total', 'Total'])]
coal_df = coal_df.dropna(subset=['State'])

# Standardize state names 
state_mapping = {
    'Maharastra': 'Maharashtra',
    'Tamilnadu': 'Tamil Nadu',
}
coal_df['State'] = coal_df['State'].str.strip().str.title()
coal_df['State'] = coal_df['State'].replace(state_mapping)

coal_df['Coal Requirement'] = pd.to_numeric(coal_df['Coal Requirement'], errors='coerce')
coal_df.dropna(subset=['Coal Requirement'], inplace=True)
# Aggregate coal requirement per state
coal_grouped = coal_df.groupby('State').agg({
    'Coal Requirement': 'sum'
}).reset_index()

coal_grouped.to_csv('cleaned_coal_plants.csv', index=False)
print(f"Saved cleaned_coal_plants.csv. Shape: {coal_grouped.shape}")
#print(f"Saved cleaned_coal_plants.csv. Shape: {coal_df.shape}")

# 3. Clean estimated-potential.csv
print("\nCleaning Estimated Potential Dataset...")
pot_df = pd.read_csv('estimated-potential.csv')

# Drop completely empty rows or 'Total' rows
pot_df = pot_df.dropna(subset=['Resource'])
pot_df = pot_df[~pot_df['Resource'].str.contains('Total', case=False, na=False)]

# Clean 'Estimated Potential (MW)' 
pot_df['Estimated Potential (MW)'] = pot_df['Estimated Potential (MW)'].astype(str).str.replace(',', '', regex=False)
pot_df['Estimated Potential (MW)'] = pd.to_numeric(pot_df['Estimated Potential (MW)'], errors='coerce')

# Drop irrelevant 'Comments' column
pot_df = pot_df[['Resource', 'Estimated Potential (MW)']]

# NOTE: This dataset only provides National aggregate potential.
# In Step 3, we will syntheticlly distribute this among states, or map it.
# Create synthetic state-wise renewable distribution

states = mop_grouped['State'].unique()

solar_total = pot_df[pot_df['Resource'].str.contains('Solar', case=False)]['Estimated Potential (MW)'].sum()
wind_total = pot_df[pot_df['Resource'].str.contains('Wind', case=False)]['Estimated Potential (MW)'].sum()

renewable_df = pd.DataFrame({
    'State': states,
    'Solar Potential (MW)': solar_total / len(states),
    'Wind Potential (MW)': wind_total / len(states)
})

renewable_df.to_csv('cleaned_renewable_potential.csv', index=False)
print(f"Saved cleaned_renewable_potential.csv. Shape: {renewable_df.shape}")

pot_df.to_csv('cleaned_estimated_potential.csv', index=False)
print(f"Saved cleaned_estimated_potential.csv. Shape: {pot_df.shape}")

# 4. Optional productconsumption.csv
print("\nSkipping productconsumption.csv as it's optional and not core to power grid modeling.")

print("\nStep 2 Cleaning Completed!")
