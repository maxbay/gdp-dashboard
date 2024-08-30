import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title and Description
st.title("Player Performance Visualization")
st.write("""
This app allows you to visualize player performance based on selected criteria. 
You can choose a player, select the data for visualization, and view the results below.
""")

# Player Selection with Autocomplete
players = ["Player A", "Player B", "Player C"]  # Replace with your player list
selected_player = st.selectbox("Select a Player", players)

# Data Selection Options
st.write("Select the data you want to visualize:")
option1 = st.checkbox("Show Data 1")
option2 = st.checkbox("Show Data 2")

# Generate Data for Visualization
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plotting the Data with Matplotlib
fig, ax = plt.subplots()
if option1:
    ax.plot(x, y1, label="Data 1")
if option2:
    ax.plot(x, y2, label="Data 2")
ax.set_title(f"Performance of {selected_player}")
ax.legend()

# Display the Plot
st.pyplot(fig)

# Explanation with LaTeX
st.write("### Calculation Details")
st.write(r"""
The data was generated using the following functions:
- For Data 1: \( y = \sin(x) \)
- For Data 2: \( y = \cos(x) \)
""")
