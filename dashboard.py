import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd

# --- USER CREDENTIALS SETUP ---
hashed_password = "$2b$12$/uWMJaA4/FSRC8InmwGjyebvKfowS1p/BjydgVpFDqjme9G6PRUsu"  # Replace with your bcrypt hash

credentials = {
    "usernames": {
        "admin": {
            "name": "Admin User",
            "password": hashed_password
        }
    }
}

# --- AUTHENTICATION SETUP ---
authenticator = stauth.Authenticate(
    credentials,
    "disaster_dashboard_cookie",
    "abcdef",
    cookie_expiry_days=1
)
# --- Page Switcher for Precautions Page ---
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# --- LOGIN ---
authenticator.login(location="main")

if st.session_state["authentication_status"]:
    if st.session_state.page == "dashboard":
        st.success(f"Welcome {st.session_state['name']}! ✅")

        st.title("🌐 Disaster Management Dashboard")
        
        st.subheader("📢 Live Disaster Feed (Simulated)")
        st.write("🚨 Thunderstorm in Delhi.")

        st.subheader("🗺️ Map View")
        disaster_location = pd.DataFrame({
            'lat': [28.6139],
            'lon': [77.2090]  # Delhi coordinates
        })
        st.map(disaster_location)

        st.subheader("📦 Resource Inventory")
        st.write("• Food Kits: 500")
        st.write("• Medical Kits: 200")
        st.write("• Rescue Teams: 50")

        # --- INVENTORY ALLOCATION ---
        st.subheader("🎯 Inventory Allocation")

        selected_location = st.selectbox("Select affected region", ["Delhi", "Mumbai", "Kolkata", "Chennai"])
        food_alloc = st.slider("Allocate Food Kits", 0, 500, 100)
        medical_alloc = st.slider("Allocate Medical Kits", 0, 200, 50)
        rescue_alloc = st.slider("Allocate Rescue Teams", 0, 50, 10)

        if st.button("Allocate Resources"):
            st.success(f"✅ Resources allocated to {selected_location}:\n"
                    f"• Food Kits: {food_alloc}\n"
                    f"• Medical Kits: {medical_alloc}\n"
                    f"• Rescue Teams: {rescue_alloc}")

        # --- WEATHER FORECAST ---
        st.subheader("☁️ Weather Forecast (Simulated)")

        weather_data = {
            "City": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
            "Temperature (°C)": [35, 30, 33, 32],
            "Humidity (%)": [45, 70, 65, 60],
            "Wind Speed (km/h)": [12, 10, 8, 15],
            "Condition": ["Sunny", "Cloudy", "Thunderstorm", "Rain"]
        }

        df_weather = pd.DataFrame(weather_data)
        st.dataframe(df_weather)

        # --- Precautions Button ---
        if st.button("📖 See Precautions"):
            st.session_state.page = "precautions"
            st.rerun()

        # --- LOGOUT ---
        authenticator.logout("Logout", "sidebar")

    # --- PRECAUTIONS PAGE ---
    elif st.session_state.page == "precautions":
        st.title("🛡️ Disaster Precautions")

        st.header("🌊 Flood Precautions")
        st.write("""
        - Move to higher ground immediately.
        - Avoid walking or driving through floodwaters.
        - Turn off gas, electricity, and water.
        """)

        st.header("🌍 Earthquake Precautions")
        st.write("""
        - Drop, Cover, and Hold On.
        - Stay away from windows.
        - If outside, move away from buildings and utility poles.
        """)

        st.header("🔥 Fire Safety")
        st.write("""
        - Stop, drop, and roll if clothes catch fire.
        - Use stairs, not elevators.
        - Keep fire extinguishers handy and accessible.
        """)

        st.header("🌪️ Thunderstorm Precautions")
        st.write("""
        - Stay indoors and secure all windows.
        - Store food and water supplies.
        - Follow official evacuation orders.
        """)

        if st.button("🔙 Back to Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

