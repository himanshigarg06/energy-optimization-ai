# ⚡ AI-Based Energy Optimization System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Problem Statement
Energy distribution across regions is inefficient, with some states facing deficits while others have stable supply. Additionally, high dependence on coal increases environmental impact.

---

## 💡 Solution
An AI-powered system that:
- Analyzes demand vs supply
- Recommends renewable energy adoption
- Optimizes energy redistribution
- Reduces coal dependency

---

## 🧠 Workflow

Data → Cleaning → Feature Engineering → ML Model → Recommendation → Optimization

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Custom Optimization Logic

---

## 📊 Results

- ⚡ **Total Energy Redistributed: 1134 MW**
- Key deficit regions handled:
  - Jammu & Kashmir
  - Kerala
  - Bihar

---

## 📈 Visualization (Optional but Recommended)

Add graphs like:
- Energy Deficit per State
- Coal Dependency Comparison

---

## 📸 Output Preview
From → To → Power Transfer
Haryana → Jammu & Kashmir → 282 MW
Delhi → Kerala → 178 MW
...
Total Redistribution: 1134 MW


---

## ⚠️ Assumptions

- Renewable potential distributed equally (data limitation)
- Surplus = 10% of available capacity
- Transfer constraints applied

---

## ❓ Viva Questions

### Q1: How is surplus calculated?
Modeled as 10% of available capacity.

### Q2: Why same renewable potential?
Due to lack of granular data.

### Q3: Why model error high?
Small + synthetic dataset; focus is optimization.

### Q4: Main contribution?
ML + decision logic + optimization system.

---

## 🚀 Setup

```bash
git clone https://github.com/himanshigarg06/energy-optimization-ai.git
cd energy-optimization-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run:
python step2_clean.py
python step3_merge.py
python step4_model.py
python step5_recommend.py
python step6_optimization.py

## Project Structure
├── step2_clean.py
├── step3_merge.py
├── step4_model.py
├── step5_recommend.py
├── step6_optimization.py
├── requirements.txt
├── README.md

##Impact
--Sustainable energy planning
--Reduced coal dependency
--Efficient power utilization

## 🎯 Conclusion
--This project demonstrates how AI can transform energy systems by combining analysis, prediction, and optimization into a unified solution.

---

# 📊 OPTIONAL: ADD GRAPH (VERY IMPRESSIVE)

## 📄 Create `visualize.py`

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('final_dataset.csv')

df.sort_values('Energy Deficit (MW)', ascending=False).head(10).plot(
    x='State', y='Energy Deficit (MW)', kind='bar'
)

plt.title("Top 10 Energy Deficit States")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("deficit_plot.png")
plt.show()

## 📊 Visualization

![Energy Deficit](deficit_plot.png)