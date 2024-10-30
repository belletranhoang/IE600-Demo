import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# Title for Streamlit app
st.title('Class Demo')

# Load the dataset
penguins = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv')

# Sidebar for category selection
st.sidebar.header('Select Options')
selected_category = st.sidebar.selectbox('Select Category', options=['All', 'Adelie', 'Gentoo', 'Chinstrap'])

# Filter data based on selection
if selected_category != 'All':
    filtered_data = penguins[penguins['species'] == selected_category]
else:
    filtered_data = penguins

# Matplotlib histogram
st.write('### Matplotlib Histogram')
fig, ax = plt.subplots()
ax.hist(filtered_data['culmen_length_mm'], bins=30, color='skyblue', edgecolor='black')
ax.set_title("Histogram of Culmen Length")
ax.set_xlabel("Culmen Length (mm)")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Seaborn density plot
st.write("### Seaborn Density Plot")
fig, ax = plt.subplots()
sns.kdeplot(filtered_data['culmen_depth_mm'], color="black", ax=ax, fill=True)
ax.set_title("Seaborn Density Plot for Culmen Depth")
ax.set_xlabel("Culmen Depth (mm)")
st.pyplot(fig)

# Altair scatter plot
st.write("### Altair Scatter Plot")
scatter_plot = alt.Chart(filtered_data).mark_circle().encode(
    x=alt.X('flipper_length_mm', title='Flipper Length (mm)'),
    y=alt.Y('body_mass_g', title='Body Mass (g)'),
    color=alt.Color('island', scale=alt.Scale(scheme='tableau10')),
    tooltip=['island', 'flipper_length_mm', 'body_mass_g']
).properties(
    width=600,
    height=400,
    title="Scatter Plot of Penguins Data"
).interactive()  # Allows zooming and panning

# Display the chart
st.altair_chart(scatter_plot, use_container_width=True)
