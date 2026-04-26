import streamlit as st

def main():
    st.title("Rpm To Speed Calculator for Mini Bikes")

    # Inputs
    f_ratio = st.number_input("Front Sprocket Teeth", value=15)
    r_ratio = st.number_input("Rear Sprocket Teeth", value=40)
    rpm = st.number_input("Engine RPM", value=5000)
    tire_size = st.number_input("Tire Diameter (Inches)", value=14.5) # Standard mini bike tire

    #calculate the gear ratio
    ratio = r_ratio / f_ratio
    #calculate the circumference of the tire
    circumference = 3.1416 * tire_size
    #calculate the speed in mph
    speed = (circumference * ratio * 60) / (ratio * 63360)

    st.divider()
    st.metric("Calculated Top Speed", f"{round(speed, 1)} MPH")
    st.write(f"Your total gear ratio is **{round(ratio, 2)}:1**")

main()