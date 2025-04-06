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
    st.subheader("Live Disaster Feed (Simulated)")
    st.write("🚨 No disasters currently reported.")
    
    st.subheader("🗺️ Map View")
    st.map()  # shows default location
    
    st.subheader("📦 Resource Inventory")
    st.write("• Food Kits: 500")
    st.write("• Medical Kits: 200")
    st.write("• Rescue Teams: 50")
    
    # Logout
    authenticator.logout("Logout", "sidebar")

elif st.session_state["authentication_status"] is False:
    st.error("❌ Incorrect username or password.")

elif st.session_state["authentication_status"] is None:
    st.warning("👋 Please enter your username and password.")
