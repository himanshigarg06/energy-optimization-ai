import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import datetime
# ================= LIVE AUTO REFRESH SETUP =================
import numpy as np
import time

# safe refresh trigger (doesn't break app)
st.query_params.update({"t": np.random.randint(0, 100000)})
# ================= PAGE CONFIG =================
st.set_page_config(page_title="Energy AI", layout="wide")

# ================= STYLING =================
st.markdown("""
<style>
body { background-color: #020617; color: white; }
h1,h2,h3 { color: white; }
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ================= LOAD DATA =================
@st.cache_data(ttl=300)
def load_data():
    url = "https://raw.githubusercontent.com/himanshigarg06/energy-optimization-ai/main/final_dataset.csv"
    return pd.read_csv(url)

df = load_data().copy()

# ================= LIVE SIMULATION =================
df["Peak Demand (MW)"] += np.random.randint(-50, 50, size=len(df))
df["Energy Deficit (MW)"] += np.random.randint(-30, 30, size=len(df))

# ================= MODEL =================
from sklearn.linear_model import LinearRegression

X = df[["Peak Demand (MW)", "Coal Dependency Ratio"]]
y = df["Energy Deficit (MW)"]

model = LinearRegression()
model.fit(X, y)

# ================= SIDEBAR =================
st.sidebar.title("⚡ Energy AI")
page = st.sidebar.radio("Navigate", ["Dashboard", "Recommendations"])

# ================= HEADER =================
st.markdown("# ⚡ AI Energy Optimization System")

st.markdown("""
<div style='padding:15px;
background: rgba(255,255,255,0.05);
border-radius:12px;'>
AI-powered system to analyze demand, predict deficits, and optimize energy distribution across India.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ================= DASHBOARD =================
if page == "Dashboard":

    # ================= LIVE CONTROL PANEL =================
    st.markdown("### 🟢 Live Data Control")

    col1, col2 = st.columns(2)

    auto_refresh = col1.checkbox("Auto Refresh (3 sec)", value=True)
    manual_refresh = col2.button("🔄 Refresh Now")

    # ================= REFRESH LOGIC =================
    if manual_refresh:
        st.cache_data.clear()
        st.rerun()

    if auto_refresh:
        time.sleep(3)
        st.rerun()
        st.success("⚡ Live system active")
        st.caption(f"Updated: {datetime.datetime.now().strftime('%H:%M:%S')}")

    # ================= KPI =================
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Deficit", round(df["Energy Deficit (MW)"].sum(),2))
    col2.metric("States", len(df))
    col3.metric("Avg Demand", round(df["Peak Demand (MW)"].mean(),2))

    st.markdown("---")

    # ================= ANALYSIS =================
    st.markdown("## 📊 Demand & Deficit Analysis")

    fig = px.bar(
        df.sort_values("Energy Deficit (MW)", ascending=False).head(10),
        x="State",
        y="Energy Deficit (MW)",
        color="Energy Deficit (MW)"
    )

    st.plotly_chart(fig, width='stretch')

    # ================= LIVE GRAPH =================
    st.markdown("## 📈 Live Demand Trend")

    values = list(df["Peak Demand (MW)"].head(20))
    fig_live = go.Figure()

    fig_live.add_trace(go.Scatter(
        y=values,
        mode='lines+markers',
        line=dict(color='cyan', width=3)
    ))

    st.plotly_chart(fig_live, width='stretch')

    # ================= FUTURE =================
    st.markdown("## 🔮 Future Forecast")

    years = st.slider("Years Ahead", 1, 10, 3)
    growth = st.slider("Demand Growth (%)", 1, 10, 5)

    df_future = df.copy()
    df_future["Peak Demand (MW)"] *= (1 + growth/100) ** years

    df_future["Future Deficit"] = model.predict(
        df_future[["Peak Demand (MW)", "Coal Dependency Ratio"]]
    )

    st.metric("Future Deficit", round(df_future["Future Deficit"].sum(),2))

    fig_future = px.bar(
        df_future.sort_values("Future Deficit", ascending=False).head(10),
        x="State",
        y="Future Deficit",
        color="Future Deficit"
    )

    st.plotly_chart(fig_future, width='stretch')

    # ================= MAP =================
    st.markdown("## 🌍 Energy Map & Flow")

    state_coords = {
        "Delhi": (28.61, 77.20),
        "Haryana": (29.06, 76.08),
        "Punjab": (31.14, 75.34),
        "Rajasthan": (27.02, 74.21),
        "Uttar Pradesh": (26.85, 80.95),
        "Bihar": (25.59, 85.13),
        "West Bengal": (22.98, 87.85),
        "Maharashtra": (19.75, 75.71),
        "Karnataka": (15.31, 75.71),
        "Kerala": (10.85, 76.27),
        "Tamil Nadu": (11.12, 78.65),
        "Telangana": (18.11, 79.01),
    }

    transfers = [
        ("Delhi", "Bihar", 80),
        ("Delhi", "Kerala", 150),
        ("Delhi", "Tamil Nadu", 60),
        ("Haryana", "Punjab", 90),
    ]

    flow_fig = go.Figure()

    # nodes
    for state, (lat, lon) in state_coords.items():
        flow_fig.add_trace(go.Scattergeo(
            lon=[lon],
            lat=[lat],
            mode='markers',
            marker=dict(size=8, color='cyan'),
        ))

    # arrows (lines)
    for src, dst, power in transfers:
        if src in state_coords and dst in state_coords:
            lat1, lon1 = state_coords[src]
            lat2, lon2 = state_coords[dst]

            flow_fig.add_trace(go.Scattergeo(
                lon=[lon1, lon2],
                lat=[lat1, lat2],
                mode='lines',
                line=dict(width=2 + power/40, color='orange'),
                opacity=0.8
            ))

    flow_fig.update_layout(
        geo=dict(
            scope='asia',
            projection_type='natural earth',
            showland=True,
            landcolor="rgb(20,20,20)"
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white")
    )

    st.plotly_chart(flow_fig, width='stretch')

    # ================= SUSTAINABILITY =================
    st.markdown("## 🌱 Sustainability")

    df["Carbon Emission"] = df["Coal Dependency Ratio"] * df["Peak Demand (MW)"] * 0.8

    st.metric("Total Emission", round(df["Carbon Emission"].sum(),2))

    fig_carbon = px.bar(
        df.sort_values("Carbon Emission", ascending=False).head(10),
        x="State",
        y="Carbon Emission",
        color="Carbon Emission"
    )

    st.plotly_chart(fig_carbon, width='stretch')

# ================= RECOMMENDATIONS =================
else:

    st.markdown("## 🤖 AI Recommendations")

    def recommend(row):
        d = row["Energy Deficit (MW)"]
        c = row["Coal Dependency Ratio"]

        if d > 100:
            return "🚨 Critical → Add renewable + import power"
        elif d > 30:
            return "⚡ Moderate → Improve distribution + reduce coal"
        elif d > 0:
            return "🔧 Low → Optimize grid"
        else:
            return "✅ Surplus → Export energy"

    df["Recommendation"] = df.apply(recommend, axis=1)

    state = st.selectbox("Select State", df["State"])
    row = df[df["State"] == state].iloc[0]

    st.metric("Deficit", row["Energy Deficit (MW)"])
    st.metric("Coal Dependency", row["Coal Dependency Ratio"])

    st.info(row["Recommendation"])

    st.markdown("### 📊 Energy Distribution")

    st.markdown("### ⚡ Energy Distribution Breakdown")

    deficit = max(row["Energy Deficit (MW)"], 0)
    demand = row["Peak Demand (MW)"]
    supply = demand - deficit

    # avoid negative values
    supply = max(supply, 0)

    fig_pie = px.pie(
        names=["Deficit ⚠️", "Supplied ✅"],
        values=[deficit, supply],
        hole=0.5
    )

    # ✨ styling
    fig_pie.update_traces(
        textinfo="percent+label",
        pull=[0.1, 0],  # highlight deficit
    )

    fig_pie.update_layout(
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title="State Energy Balance"
    )

    st.plotly_chart(fig_pie, width='stretch')

# ================= FOOTER =================
st.markdown("---")
st.markdown("Made with ⚡ by Himanshi")