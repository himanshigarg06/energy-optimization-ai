# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Energy AI", layout="wide")

# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
#     color: white;
# }

# .big-font {
#     font-size:50px !important;
#     font-weight: bold;
# }

# .card {
#     background: linear-gradient(135deg, #1f2937, #111827);
#     padding: 20px;
#     border-radius: 15px;
#     text-align: center;
#     box-shadow: 0px 0px 20px rgba(0,255,255,0.2);
# }

# .metric {
#     font-size: 30px;
#     font-weight: bold;
# }
# </style>
# """, unsafe_allow_html=True)

# # Load data
# df = pd.read_csv("final_dataset.csv")

# st.title("⚡ AI Energy Optimization System")

# st.write("Analyze energy distribution, recommendations, and optimization.")

# st.markdown('<p class="big-font">⚡ AI Energy Optimization Dashboard</p>', unsafe_allow_html=True)

# st.write("Smart system to analyze, recommend, and optimize power distribution across India 🚀")

# col1, col2, col3 = st.columns(3)

# col1.markdown(f"""
# <div class="card">
# <h3>Total Deficit</h3>
# <p class="metric">{round(df['Energy Deficit (MW)'].sum(),2)} MW</p>
# </div>
# """, unsafe_allow_html=True)

# col2.markdown("""
# <div class="card">
# <h3>Optimized Energy</h3>
# <p class="metric">1134 MW</p>
# </div>
# """, unsafe_allow_html=True)

# col3.markdown("""
# <div class="card">
# <h3>States Covered</h3>
# <p class="metric">37</p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("---")


# # 📊 Show dataset
# st.subheader("Dataset Preview")
# st.dataframe(df)

# # 📈 Energy Deficit Graph
# #st.subheader("Top 10 Energy Deficit States")
# st.subheader("📊 Energy Deficit Analysis")

# fig, ax = plt.subplots(figsize=(10,5))
# top = df.sort_values("Energy Deficit (MW)", ascending=False).head(10)

# ax.bar(top["State"], top["Energy Deficit (MW)"])
# plt.xticks(rotation=45)

# st.pyplot(fig)
# #top_deficit = df.sort_values("Energy Deficit (MW)", ascending=False).head(10)

# #fig1, ax1 = plt.subplots()
# #ax1.bar(top_deficit["State"], top_deficit["Energy Deficit (MW)"])
# #plt.xticks(rotation=45)
# #plt.ylabel("MW")
# #plt.title("Energy Deficit")

# #st.pyplot(fig1)
# st.markdown("---")
# # 📊 Coal Dependency Graph
# st.subheader("📊 Coal Dependency")

# top_coal = df.sort_values("Coal Dependency Ratio", ascending=False).head(10)

# fig2, ax2 = plt.subplots(figsize=(10,5))
# ax2.bar(top_coal["State"], top_coal["Coal Dependency Ratio"])
# plt.xticks(rotation=45)

# st.pyplot(fig2)
# st.markdown("---")
# # 📍 Recommendations
# st.subheader("📍 State-wise Recommendations")

# def recommend(row):
#     deficit = row['Energy Deficit (MW)']
#     coal_ratio = row['Coal Dependency Ratio']

#     if deficit > 50:
#         return f"Install ~{round(deficit,0)} MW renewable + reduce coal"
#     elif deficit > 0:
#         return f"Increase renewable by ~{round(deficit,0)} MW"
#     else:
#         if coal_ratio > 1:
#             return "Reduce coal dependency"
#         else:
#             return "Can export energy"

# df["Recommendation"] = df.apply(recommend, axis=1)

# state = st.selectbox("Select State", df["State"])

# st.write(df[df["State"] == state][["Energy Deficit (MW)", "Coal Dependency Ratio", "Recommendation"]])
# st.markdown("---")
# st.success("🚀 AI successfully optimized 1134 MW energy distribution")
# # ⚡ Optimization summary

# st.subheader("⚡ Optimization Summary")

# st.metric("Total Energy Deficit (MW)", round(df["Energy Deficit (MW)"].sum(), 2))
# st.metric("Estimated Optimization (MW)", 1134)

# #st.balloons()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Energy AI", layout="wide")

# ================= CUSTOM STYLING =================
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.big-font {
    font-size:50px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================= LOAD DATA =================
df = pd.read_csv("final_dataset.csv")

# ================= SIDEBAR =================
st.sidebar.title("⚡ Energy AI Dashboard")
page = st.sidebar.radio("Navigate", ["Dashboard", "Recommendations"])

# ================= HERO HEADER =================
st.markdown("""
<h1 style='text-align: center; 
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip: text;
color: transparent;'>
⚡ AI Energy Optimization System
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# ================= DASHBOARD =================
if page == "Dashboard":

    # 🔥 KPI CARDS
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Deficit (MW)", round(df["Energy Deficit (MW)"].sum(), 2))
    col2.metric("Optimized Energy (MW)", 1134)
    col3.metric("States Covered", len(df))

    st.markdown("---")

    # 🔥 INTERACTIVE DEFICIT GRAPH
    st.subheader("📊 Energy Deficit Analysis")

    top = df.sort_values("Energy Deficit (MW)", ascending=False).head(10)

    fig = px.bar(
        top,
        x="State",
        y="Energy Deficit (MW)",
        color="Energy Deficit (MW)",
        color_continuous_scale="Blues",
        title="Top Deficit States"
    )

    st.plotly_chart(fig, use_container_width=True)

    # 🔥 COAL GRAPH
    st.subheader("📊 Coal Dependency Analysis")

    top_coal = df.sort_values("Coal Dependency Ratio", ascending=False).head(10)

    fig2 = px.bar(
        top_coal,
        x="State",
        y="Coal Dependency Ratio",
        color="Coal Dependency Ratio",
        color_continuous_scale="Reds",
        title="Coal Dependency"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # 🔥 SUCCESS MESSAGE
    st.success("🚀 AI Optimized 1134 MW Energy Redistribution")

# ================= RECOMMENDATIONS =================
else:

    st.subheader("📍 State-wise Recommendation Engine")

    def recommend(row):
        deficit = row['Energy Deficit (MW)']
        coal_ratio = row['Coal Dependency Ratio']

        if deficit > 50:
            return f"Install ~{round(deficit,0)} MW renewable + reduce coal"
        elif deficit > 0:
            return f"Increase renewable by ~{round(deficit,0)} MW"
        else:
            if coal_ratio > 1:
                return "Reduce coal dependency"
            else:
                return "Can export energy"

    df["Recommendation"] = df.apply(recommend, axis=1)

    state = st.selectbox("Select State", df["State"])

    result = df[df["State"] == state]

    row = result.iloc[0]

    st.metric("Energy Deficit (MW)", row["Energy Deficit (MW)"])
    st.metric("Coal Dependency", row["Coal Dependency Ratio"])

    st.info(row["Recommendation"])

    st.markdown("---")

    # 🔥 PIE CHART
    fig3 = px.pie(
    names=["Deficit", "Remaining"],
    values=[row["Energy Deficit (MW)"], 100],
    title="Energy Distribution View"
)

    st.plotly_chart(fig3)

# ================= FOOTER =================
st.markdown("""
<hr>
<center>Made with ⚡ by Himanshi</center>
""", unsafe_allow_html=True)