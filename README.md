# ⚡ AI-Based Energy Optimization System

## 📌 Problem Statement
Energy distribution across regions is often inefficient, with some states facing power deficits while others have stable or surplus supply. Additionally, heavy dependence on coal-based energy increases environmental impact.

---

## 💡 Solution
This project presents an **AI-powered energy optimization system** that:

- Analyzes energy demand and supply across states
- Identifies deficit and stable regions
- Recommends renewable energy adoption
- Optimizes electricity redistribution across states
- Reduces dependency on coal-based energy

---

## 🧠 Approach / Workflow

Data Collection → Data Cleaning → Feature Engineering → ML Model → Recommendation System → Optimization Engine

### 🔹 Steps:

1. **Data Cleaning**
   - Processed energy availability, coal usage, and renewable datasets
   - Removed inconsistencies and standardized state names

2. **Feature Engineering**
   - Energy Deficit = Demand - Supply
   - Coal Dependency Ratio
   - Renewable Potential

3. **Machine Learning Model**
   - Used Random Forest Regressor
   - Predicted energy deficit trends

4. **Recommendation System**
   - Suggests:
     - Renewable installation (MW)
     - Coal reduction strategies
     - Energy export opportunities

5. **Optimization Engine (Core)**
   - Redistributes power from stable states to deficit states
   - Uses constrained transfer logic

---

## ⚙️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Custom optimization logic  

---

## 📊 Results

- ⚡ **Total Energy Redistributed: 1134 MW**
- High-deficit states addressed:
  - Jammu & Kashmir
  - Kerala
  - Bihar

---

## 📈 Example Output

From → To → Power Transfer  
Haryana → Jammu & Kashmir → 282 MW  
Delhi → Kerala → 178 MW  
...  
Total Redistribution: 1134 MW  

---

## ⚠️ Assumptions

- Renewable potential is distributed equally across states due to lack of granular data  
- Surplus energy is modeled as **10% of available capacity**  
- Transfer limits applied to avoid over-dependence on a single state  

---

## ❓ Common Questions (Viva Ready)

### Q1: How is surplus energy calculated?
We modeled surplus as 10% of available generation capacity due to lack of explicit surplus data.

### Q2: Why is renewable potential same for all states?
Due to lack of state-wise data, we used proportional distribution for consistency.

### Q3: Why is model accuracy high/low?
The dataset is small and partially synthetic. The model demonstrates predictive capability, while the main contribution is optimization.

### Q4: What is the main contribution?
Integration of ML + decision logic + optimization to solve real-world energy distribution problems.

### Q5: Can this be used in real life?
Yes. With real-time grid and renewable data, this can be extended into a real-world smart grid optimization system.

---

## 🚀 Setup Instructions

### 1. Clone repository
git clone https://github.com/your-username/energy-optimization-ai.git  
cd energy-optimization-ai  

### 2. Create virtual environment
python3 -m venv venv  

### 3. Activate environment
source venv/bin/activate  

### 4. Install dependencies
pip install -r requirements.txt  

### 5. Run project
python step2_clean.py  
python step3_merge.py  
python step4_model.py  
python step5_recommend.py  
python step6_optimization.py  

---

## 📁 Project Structure

energy-optimization-ai/  
│  
├── step2_clean.py  
├── step3_merge.py  
├── step4_model.py  
├── step5_recommend.py  
├── step6_optimization.py  
├── requirements.txt  
├── README.md  

---

## 🌍 Impact

- Reduces coal dependency  
- Improves energy efficiency  
- Supports renewable adoption  
- Helps in smart grid planning  

---

## 🎯 Conclusion

This project demonstrates how AI can be used to **analyze, recommend, and optimize energy systems**, making it a step toward sustainable and efficient power management.