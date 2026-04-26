import streamlit as st
import math

st.title("Mini Bike Speed Calculator")

def speed_calculator():

    # Inputs
    f_ratio = st.number_input("Front Sprocket Teeth (Teeth)", value=12)
    r_ratio = st.number_input("Rear Sprocket Teeth (Teeth)", value=75)
    rpm = st.number_input("Engine RPM", value=3600)
    tire_size = st.number_input("Tire Diameter (Inches)", value=14) 

    #calculate the gear ratio
    ratio = r_ratio / f_ratio
    #calculate the circumference of the tire
    circumference = 3.1416 * tire_size
    #calculate the speed in mph
    speed = (rpm * circumference * 60) / (ratio * 63360)

    st.divider()
    st.metric("Calculated Top Speed", f"{round(speed_calculator(), 1)} MPH")

def rpm_calculator():

    # inputs
    f_ratio = st.number_input("Front Sprocket Teeth (Teeth)", value=12)
    r_ratio = st.number_input("Rear Sprocket Teeth (Teeth)", value=75)
    speed = st.number_input("Speed (MPH)", value=20)
    tire_size = st.number_input("Tire Diameter (Inches)", value=14)

    # calculate the gear ratio
    ratio = r_ratio / f_ratio
    # calculate the circumference of the tire
    circumference = 3.1416 * tire_size
    # calculate the engine RPM
    rpm = (speed * ratio * 63360) / (circumference * 60)

    st.divider()
    st.metric("Engine RPM At Given Speed", f"{round(rpm, 1)} RPM")

def gear_ratio_calculator():

    # inputs
    f_ratio = st.number_input("Front Sprocket Teeth (Teeth)", value=12)
    r_ratio = st.number_input("Rear Sprocket Teeth (Teeth)", value=75)

    # calculate the gear ratio
    ratio = r_ratio / f_ratio
    st.divider()
    st.metric("Gear Ratio", f"{round(ratio, 2)} : 1")

calculator = st.radio("Select Calculator", ["Speed", "RPM", "Gear Ratio"])

if calculator == "Speed":
    speed_calculator()
elif calculator == "RPM":
    rpm_calculator()
else:
    gear_ratio_calculator()




