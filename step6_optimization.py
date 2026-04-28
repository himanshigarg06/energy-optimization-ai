import pandas as pd

import numpy as np

# ================= LIVE DATA =================
url = "https://raw.githubusercontent.com/himanshigarg06/energy-optimization-ai/main/final_dataset.csv"

@st.cache_data(ttl=300)  # refresh every 5 minutes
def load_data():
    df = pd.read_csv(url)
    
    # simulate small real-time fluctuation
    df["Peak Demand (MW)"] += np.random.randint(-20, 20, size=len(df))
    df["Energy Deficit (MW)"] += np.random.randint(-10, 10, size=len(df))
    
    return df

df = load_data()

# Separate deficit and surplus states
deficit_states = df[df['Energy Deficit (MW)'] > 0].copy()
# Simulate surplus from states with zero deficit
surplus_states = df[df['Energy Deficit (MW)'] == 0].copy()

# Assume each surplus state can provide 10% of its peak supply
surplus_states['Available Surplus (MW)'] = surplus_states['Peak Met (MW)'] * 0.1

transfers = []

# Limit how much each state can give (max 30% of its surplus)
surplus_states['Max Transfer'] = surplus_states['Available Surplus (MW)'] * 0.3 

for i, d_row in deficit_states.iterrows():
    remaining_deficit = d_row['Energy Deficit (MW)']

    for j, s_row in surplus_states.iterrows():
        available = min(
    s_row['Available Surplus (MW)'],
    s_row['Max Transfer']
)

        if available > 0 and remaining_deficit > 0:
            transfer = min(remaining_deficit, available)

            transfers.append({
                'From': s_row['State'],
                'To': d_row['State'],
                'Power Transfer (MW)': round(transfer, 2)
            })

            remaining_deficit -= transfer

            # Update surplus after transfer
            surplus_states.at[j, 'Available Surplus (MW)'] -= transfer

        if remaining_deficit <= 0:
            break

# Convert to dataframe
# Convert to dataframe FIRST
transfer_df = pd.DataFrame(transfers)

# THEN sort
if not transfer_df.empty:
    transfer_df = transfer_df.sort_values(by='Power Transfer (MW)', ascending=False)

print("\n--- OPTIMIZED ENERGY TRANSFER PLAN ---\n")
print(transfer_df)

total_transfer = transfer_df['Power Transfer (MW)'].sum()

print("\nTotal Power Redistributed:", round(total_transfer, 2), "MW")