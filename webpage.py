import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data.db")

st.header('Average Global Temperature')

user_slider_choice = st.slider('Number of values', min_value=1, max_value=10, step=1)


# EXTRACT THE DATA FROM DATABASE
def load_data(user_choice):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM temperature "
                   "ORDER BY time DESC "
                   f"LIMIT {user_choice}")
    rows = cursor.fetchall()
    temperatures = [i[1] for i in rows]
    times = [i[2] for i in rows]
    print(f'{times} -- {temperatures}')
    return times, temperatures


# PLOT THE CHART
def plot_chart(times, temperatures):
    figure = px.line(x=times, y=temperatures, labels={'x': 'Time', 'y': 'Temperature (C)'})
    st.plotly_chart(figure)


times, temperatures = load_data(user_slider_choice)
plot_chart(times, temperatures)
