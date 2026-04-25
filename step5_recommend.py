import pandas as pd

df = pd.read_csv('final_dataset.csv')

def recommend(row):
    deficit = row['Energy Deficit (MW)']
    coal_ratio = row['Coal Dependency Ratio']

    if deficit > 50:
        if coal_ratio > 1:
            return f"High deficit ({round(deficit,2)} MW) with high coal dependency. Install ~{round(deficit,0)} MW solar/wind and reduce coal usage."
        else:
            return f"High deficit ({round(deficit,2)} MW). Install ~{round(deficit,0)} MW solar/wind capacity."

    elif deficit > 0:
        if coal_ratio > 1:
            return f"Moderate deficit ({round(deficit,2)} MW) and high coal dependency. Increase renewables and reduce coal usage."
        else:
            return f"Moderate deficit ({round(deficit,2)} MW). Increase renewable usage by ~{round(deficit,0)} MW."

    else:
        if coal_ratio > 1:
            return "No deficit but high coal dependency. Replace coal plants with renewable sources gradually."
        else:
            return "Surplus energy. Can export power to deficit states."

df['Recommendation'] = df.apply(recommend, axis=1)

print("\n--- STATE-WISE RECOMMENDATIONS ---\n")
print(df[['State', 'Energy Deficit (MW)', 'Coal Dependency Ratio', 'Recommendation']])