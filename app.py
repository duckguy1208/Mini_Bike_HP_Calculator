import streamlit as st

def main():
    st.title("⚙️ Speed-to-HP Analyzer")

    # Inputs
    mph = st.number_input("Top Speed Reached (MPH)", value=40)
    f_ratio = st.number_input("Front Sprocket Teeth", value=15)
    r_ratio = st.number_input("Rear Sprocket Teeth", value=40)
    ratio = r_ratio / f_ratio
    tire_size = st.number_input("Tire Diameter (Inches)", value=14.5) # Standard mini bike tire

    # 1. Calculate RPM
    rpm = (mph * ratio * 336) / tire_size

    # 2. Estimate HP based on Drag
    # (Note: This is a simplified estimate for small bikes)
    estimated_hp = (mph / 19)**3 

    st.divider()
    col1, col2 = st.columns(2)
    col1.metric("Engine RPM", f"{int(rpm)}")
    col2.metric("Estimated HP", f"{round(estimated_hp, 1)} hp")

    # Gearhead Logic
    if rpm > 5500:
        st.warning("⚠️ You're screaming! You might need a smaller rear sprocket.")
    elif rpm < 3500:
        st.info("🛠️ You've got room to gear it down for more torque!")

main()