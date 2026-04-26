import streamlit as st
import math

st.title("Speed Calculator for Mini Bikes")

# Inputs
f_ratio = st.number_input("Front Sprocket Teeth (Teeth)", value=12)
r_ratio = st.number_input("Rear Sprocket Teeth (Teeth)", value=75)
rpm = st.number_input("Engine RPM", value=3600)
tire_size = st.number_input("Tire Diameter (Inches)", value=12) 

#calculate the gear ratio
ratio = r_ratio / f_ratio
#calculate the circumference of the tire
circumference = 3.1416 * tire_size
#calculate the speed in mph
speed = (rpm * circumference * 60) / (ratio * 63360)

st.divider()
st.write("Calculated Top Speed", f"{speed:.1f} MPH")


