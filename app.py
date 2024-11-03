import streamlit as st

st.subheader("T E M P E R A T U R E  -  C O N V E R T E R")
st.write("")
st.write("-- a basic app to demonstrate session state in streamlit --" )
st.subheader("")

#initialize state with temperatures

if "celcius" not in st.session_state:
    st.session_state["celcius"] = 0.00
if "kelvin" not in st.session_state:
    st.session_state["kelvin"] = 273.15
if "farenheit" not in st.session_state:
    st.session_state["farenheit"] = 32.00

# conversion functions

def celcius_conversion():
    celcius = st.session_state["celcius"]
    st.session_state["farenheit"] = (celcius * 9/5) + 32
    st.session_state["kelvin"] = celcius + 273.15

def farenheit_conversion():
    farenheit = st.session_state["farenheit"]
    st.session_state["celcius"] = (farenheit - 32) * 5/9
    st.session_state["kelvin"] = (farenheit - 32) * 5/9 + 273.15

def kelvin_conversion():
    kelvin = st.session_state["kelvin"]
    st.session_state["celcius"] = kelvin - 273.15
    st.session_state["farenheit"] = (kelvin - 273.15) * 9/5 

# callback for user input number
def add_to_celcius(num):
    st.session_state["celcius"] += num
    celcius_conversion()

def set_temperatures(celcius, farenheit, kelvin):
    st.session_state["celcius"] = celcius
    st.session_state["farenheit"] = farenheit
    st.session_state["kelvin"] = kelvin

col1, col2, col3 = st.columns(3)

col1.number_input("Celcius", step=0.01, key="celcius", on_change=celcius_conversion)
col2.number_input("Farenheit", step=0.01, key="farenheit", on_change=farenheit_conversion)
col3.number_input("Kelvin", step=0.01, key="kelvin", on_change=kelvin_conversion)


col1, _, _, = st.columns(3)
num = col1.number_input("Add to Celcius", step=1)
col1.button("Add", type="primary", on_click=add_to_celcius, args=(num,))

col1, col2, col3 = st.columns(3)
col1.button("🧊 Freezing Point of Water", on_click=set_temperatures, kwargs=dict(celcius=0.00, farenheit=32.00, kelvin=273.15))
col2.button("🔥 Boiling Point of Water", on_click=set_temperatures, kwargs=dict(celcius=100.00, farenheit=212.00, kelvin=373.15))
col3.button("⚡️ Absolute Zero", on_click=set_temperatures, kwargs=dict(celcius=-273.15, farenheit=491.67, kelvin=273.15))

st.title("")
st.write(st.session_state)