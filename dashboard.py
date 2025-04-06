import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# --- USER CREDENTIALS SETUP ---
# Replace with your generated bcrypt hash (from hash_generator.py)
hashed_password = "$2b$12$/uWMJaA4/FSRC8InmwGjyebvKfowS1p/BjydgVpFDqjme9G6PRUsu"  # replace with your hash

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

# --- LOGIN ---
authenticator.login(location="main")

if st.session_state["authentication_status"]:
    st.success(f"Welcome {st.session_state['name']}! ✅")
    
    st.title("🌐 Disaster Management Dashboard")
    st.write("🚨 Thunderstorm reported in Delhi!")

    st.subheader("🗺️ Map View")

    import pandas as pd

# Disaster location: Delhi (You can replace with dynamic coordinates later)
    disaster_location = pd.DataFrame({
      'lat': [28.6139],
      'lon': [77.2090]
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

 
    
    # Logout
    authenticator.logout("Logout", "sidebar")

elif st.session_state["authentication_status"] is False:
    st.error("❌ Incorrect username or password.")

elif st.session_state["authentication_status"] is None:
    st.warning("👋 Please enter your username and password.")
