import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="🚀 Rocket Engineering Dashboard", layout="wide")

# ---------------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------------

st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
h1, h2, h3 {
    color: #00D4FF;
}
.stMetric {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown("# 🚀 Rocket Launch Engineering Dashboard")
st.markdown("### Aerospace Data Analysis + Physics-Based Simulation")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
    use_container_width=True
)

st.markdown("""
This dashboard integrates real mission data with differential equation modeling 
to simulate real-world rocket launch dynamics.
""")

st.divider()

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("space_missions.csv")

df = load_data()

# CLEAN DATA
if "Launch Date" in df.columns:
    df["Launch Date"] = pd.to_datetime(df["Launch Date"], errors="coerce")

numeric_cols = [
    "Mission Cost",
    "Payload Weight",
    "Fuel Consumption",
    "Mission Duration",
    "Distance from Earth",
    "Crew Size",
    "Scientific Yield"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna()
df = df.drop_duplicates()

# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------

tab1, tab2, tab3 = st.tabs(
    ["📊 Mission Analytics", "🧮 Rocket Simulation", "📈 Engineering Insights"]
)

# =========================================================
# TAB 1 — DATA ANALYSIS
# =========================================================

with tab1:

    st.subheader("Mission Dataset Overview")

    col1, col2, col3 = st.columns(3)

    success_rate = (df["Mission Success"] == "Success").mean() * 100
    avg_cost = df["Mission Cost"].mean()
    avg_payload = df["Payload Weight"].mean()

    col1.metric("Mission Success Rate (%)", round(success_rate, 2))
    col2.metric("Average Mission Cost", round(avg_cost, 2))
    col3.metric("Average Payload Weight (kg)", round(avg_payload, 2))

    st.divider()

    mission_type = st.selectbox(
        "Filter by Mission Type",
        df["Mission Type"].unique()
    )

    filtered_df = df[df["Mission Type"] == mission_type]

    # Scatter Plot
    fig1 = px.scatter(
        filtered_df,
        x="Payload Weight",
        y="Fuel Consumption",
        color="Mission Success",
        title="Payload vs Fuel Consumption",
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Bar Chart
    cost_summary = (
        filtered_df.groupby("Mission Success")["Mission Cost"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        cost_summary,
        x="Mission Success",
        y="Mission Cost",
        title="Mission Cost by Success",
        color="Mission Success"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Line Plot
    fig3 = px.line(
        filtered_df,
        x="Distance from Earth",
        y="Mission Duration",
        title="Mission Duration vs Distance",
        color_discrete_sequence=["#00D4FF"]
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Box Plot
    fig4 = px.box(
        filtered_df,
        x="Mission Success",
        y="Crew Size",
        title="Crew Size Distribution",
        color="Mission Success"
    )
    st.plotly_chart(fig4, use_container_width=True)

    # Scientific Yield vs Cost
    fig5 = px.scatter(
        filtered_df,
        x="Mission Cost",
        y="Scientific Yield",
        color="Mission Success",
        title="Scientific Yield vs Mission Cost"
    )
    st.plotly_chart(fig5, use_container_width=True)

    # Correlation Heatmap
    corr = filtered_df.corr(numeric_only=True)
    fig6 = px.imshow(corr, text_auto=True, title="Correlation Matrix")
    st.plotly_chart(fig6, use_container_width=True)

# =========================================================
# TAB 2 — ROCKET SIMULATION
# =========================================================

with tab2:

    st.subheader("Physics-Based Rocket Launch Simulation")

    payload = st.slider("Payload (kg)", 1000, 50000, 10000)
    thrust = st.slider("Thrust (N)", 1000000, 15000000, 7000000)

    g = 9.81
    dt = 1
    time_steps = 200
    fuel_burn_rate = 2000
    k = 0.00002

    mass = 500000 + payload
    velocity_drag = 0
    altitude_drag = 0
    velocity_no_drag = 0
    altitude_no_drag = 0

    results_drag = []
    results_no_drag = []

    for t in range(time_steps):

        drag = k * velocity_drag**2
        a_drag = (thrust - mass * g - drag) / mass
        velocity_drag += a_drag * dt
        altitude_drag += velocity_drag * dt

        a_no_drag = (thrust - mass * g) / mass
        velocity_no_drag += a_no_drag * dt
        altitude_no_drag += velocity_no_drag * dt

        mass -= fuel_burn_rate

        if mass <= 0:
            break

        results_drag.append([t, altitude_drag])
        results_no_drag.append([t, altitude_no_drag])

    sim_drag = pd.DataFrame(results_drag, columns=["Time", "Altitude"])
    sim_no_drag = pd.DataFrame(results_no_drag, columns=["Time", "Altitude"])

    fig_compare = px.line(title="Altitude Comparison: With vs Without Drag")
    fig_compare.add_scatter(
        x=sim_drag["Time"],
        y=sim_drag["Altitude"],
        name="With Drag"
    )
    fig_compare.add_scatter(
        x=sim_no_drag["Time"],
        y=sim_no_drag["Altitude"],
        name="Without Drag"
    )
    st.plotly_chart(fig_compare, use_container_width=True)

    colA, colB = st.columns(2)
    colA.metric("Max Altitude (With Drag)", round(sim_drag["Altitude"].max(), 2))
    colB.metric("Max Altitude (No Drag)", round(sim_no_drag["Altitude"].max(), 2))

# =========================================================
# TAB 3 — INSIGHTS
# =========================================================

with tab3:

    st.subheader("Engineering Interpretation")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
        use_container_width=True
    )

    st.markdown("""
### Key Aerospace Insights:

- Increasing payload increases required fuel.
- Drag significantly reduces maximum altitude.
- Higher thrust improves acceleration but increases fuel burn.
- Mission cost does not always guarantee success.
- Scientific yield does not scale linearly with spending.
    """)

    st.markdown("""
This system combines real-world mission analytics with a differential equation model 
to simulate rocket dynamics under varying engineering conditions.
""")
