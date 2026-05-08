import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
from datetime import datetime
import time

# --- PLATFORM CONFIGURATION ---
st.set_page_config(
    page_title="UrbanPulse AI Platform",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- AI STRESS LOGIC ENGINE ---
def calculate_urban_stress(pop, w_cond, t_cycle, emergency):
    base = 30
    w_map = {"Clear Skies": 0, "Heavy Rain": 15, "Severe Storm": 35}
    t_map = {"Morning Peak": 20, "Mid-Day": 5, "Evening Peak": 25, "Night": -10}
    
    total = base + pop//2 + w_map[w_cond] + t_map[t_cycle]
    if emergency: total += 40
    return min(max(total, 5), 100)

# --- SIDEBAR CONTROL CENTER ---
with st.sidebar:
    st.title("🎛️ Simulation Suite")
    st.markdown("---")
    sim_pop = st.slider("Population Load (%)", 0, 100, 25)
    sim_weather = st.selectbox("Weather Model", ["Clear Skies", "Heavy Rain", "Severe Storm"])
    sim_time = st.select_slider("Temporal Cycle", options=["Morning Peak", "Mid-Day", "Evening Peak", "Night"])
    sim_emergency = st.toggle("🚨 Trigger Emergency Protocol")
    
    st.markdown("---")
    hourly_loss = (calculate_urban_stress(sim_pop, sim_weather, sim_time, sim_emergency) * 1250)
    st.metric("Economic Impact (Hourly)", f"${hourly_loss:,}", delta="Fiscal Drag", delta_color="inverse")
    st.caption("UrbanPulse Core Engine v3.1.0")

global_stress = calculate_urban_stress(sim_pop, sim_weather, sim_time, sim_emergency)

# --- HEADER ---
st.title("🏙️ UrbanPulse AI Infrastructure Hub")
st.markdown(f"**Operational Intelligence Dashboard** | System Status: {'⚠️ CRITICAL' if global_stress > 75 else '✅ NOMINAL'}")

# --- WEB APP NAVIGATION TABS ---
tab_map, tab_analytics, tab_vision, tab_sos = st.tabs([
    "🌐 Geospatial Heatmap", 
    "📊 Predictive Analytics", 
    "👁️ Visual Surveillance",
    "🆘 Emergency SOS System"
])

# (Maps and Analytics sections remain the same as previous version)
with tab_map:
    st.subheader("Real-Time Stress Visualization")
    m_col1, m_col2 = st.columns([3, 1])
    with m_col1:
        map_data = pd.DataFrame(np.random.randn(250, 2) / [60, 60] + [37.7749, -122.4194], columns=['lat', 'lon'])
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/dark-v9',
            initial_view_state=pdk.ViewState(latitude=37.7749, longitude=-122.4194, zoom=12, pitch=50),
            layers=[pdk.Layer('HexagonLayer', data=map_data, get_position='[lon, lat]', radius=200, elevation_scale=global_stress * 4, extruded=True, get_fill_color=f"[255, {max(250 - global_stress*2, 0)}, 0, 160]")]
        ))
    with m_col2:
        st.write("### Sector KPIs")
        st.metric("Live Stress Index", f"{global_stress}%")
        st.metric("Revenue Leakage", f"${int(hourly_loss/60)}/min")

with tab_analytics:
    st.subheader("Data Forecasting Models")
    a_col1, a_col2 = st.columns(2)
    with a_col1:
        fig = go.Figure(go.Indicator(mode="gauge+number", value=global_stress, gauge={'bar': {'color': "#00ffa2"}}))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
        st.plotly_chart(fig, use_container_width=True)
    with a_col2:
        chart_data = pd.DataFrame(np.random.randn(20, 2) + [global_stress/10, global_stress/10 + 2], columns=['Historical', 'AI Prediction'])
        st.line_chart(chart_data)

with tab_vision:
    st.subheader("Computer Vision: Traffic Node Feeds")
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.image("https://images.unsplash.com/photo-1545147986-a9d6f210df77?auto=format&fit=crop&w=800&q=80", caption="Node 07: Live Feed")
    with v_col2:
        st.image("https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=800&q=80", caption="Node 12: Financial District")

# --- FEATURE: EMERGENCY SOS SYSTEM ---
with tab_sos:
    st.subheader("🆘 SOS Response Command Center")
    
    s_col1, s_col2 = st.columns([2, 1])
    
    with s_col1:
        st.markdown("### Critical Incident Log")
        # Creating a fake live incident log
        incidents = pd.DataFrame({
            "Incident ID": ["SOS-992", "SOS-981", "SOS-977"],
            "Location": ["Sector 7 (Main St)", "Sector 2 (Industrial)", "Sector 4 (Downtown)"],
            "Severity": ["🔴 CRITICAL", "🟡 MODERATE", "🟢 RESOLVED"],
            "AI Priority": [1, 2, 5]
        })
        st.table(incidents)
        
        # Interactive SOS Trigger
        st.warning("Manual Override: Use only in case of mass-infrastructure failure.")
        if st.button("🔥 INITIATE CITY-WIDE SOS PROTOCOL"):
            st.error("CITY-WIDE SOS INITIALIZED. ALL NON-EMERGENCY SERVICES HALTED.")
            with st.status("Deploying Rapid Response Units...", expanded=True) as status:
                st.write("Isolating affected power grids...")
                time.sleep(1)
                st.write("Overriding traffic light cycles for emergency corridors...")
                time.sleep(1)
                st.write("Establishing secure satellite uplink with First Responders...")
                status.update(label="Units Deployed. Real-time tracking active.", state="complete")
            st.balloons() # Visual feedback for successful "save"
            
    with s_col2:
        st.markdown("### Unit Deployment")
        # Simulated Unit Tracking
        st.write("**Active Units:**")
        st.info("🚑 Ambulance: 12 Units (On-Route)")
        st.info("🚒 Fire Response: 04 Units (Standby)")
        st.info("👮 Police: 08 Units (In-Zone)")
        
        # Live "Signal" Simulation
        st.write("**Secure Link Status:**")
        st.success("🛰️ Satellite Uplink: CONNECTED")
        st.success("📡 Mesh Network: OPTIMAL")

st.markdown("---")
st.caption("UrbanPulse AI Platform | v3.1 SOS Edition | Bangalore Hackathon 2026")