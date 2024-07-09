import streamlit as st
import plotly.express as px

st.header('Average Global Temperature')

days = st.slider('Number of days', min_value=1, max_value=7, step=1)


# EXTRACT THE DATA FROM TEXT FILE
def load_data(user_days):
    with open('data.txt', 'r') as f:
        all_data = f.readlines()
        data = all_data[-user_days:]

        times = [line[:-4] for line in data]
        temperatures = [line[-3:-1] for line in data]
        return times, temperatures


# PLOT THE CHART
def plot_chart(times, temperatures):
    figure = px.line(x=times, y=temperatures, labels={'x':'Date', 'y': 'Temperature (C)'})
    st.plotly_chart(figure)


times, temperature = load_data(days)
plot_chart(times, temperature)
