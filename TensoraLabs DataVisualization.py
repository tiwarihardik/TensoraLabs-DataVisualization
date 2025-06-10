import seaborn as sns 
import matplotlib.pyplot as plt 
import streamlit as st
import pandas as pd 

st.title("TensoraLabs - Data Visualization")
st.write("Visualize your data and make key inferences from it.")

dataset = st.file_uploader("CSV or Excel File: ", type=['csv', 'xlsx'])

if dataset is not None:
    if dataset.name.endswith(".xlsx"):
        dataset_ = pd.read_excel(dataset)  
    else:
        dataset_ = pd.read_csv(dataset)  

    st.write(dataset_.head())
    
    dv_technique = st.selectbox("Choose a technique: ", ['Scatter Plot', 'Line Plot', 'Histogram', 'Bar Graph'])

    x_axis = st.selectbox("Select x-axis column:", list(dataset_.columns))
    y_axis = None
    if dv_technique != "Histogram":
        y_axis = st.selectbox("Select y-axis column:", list(dataset_.columns))

    if st.button("Plot the graph"):
        plt.figure(figsize=(10, 5))
        if dv_technique == 'Scatter Plot':
            sns.scatterplot(data=dataset_, x=x_axis, y=y_axis)
            st.balloons()
        elif dv_technique == 'Line Plot':
            sns.lineplot(data=dataset_, x=x_axis, y=y_axis)
            st.balloons()
        elif dv_technique == 'Histogram':
            sns.histplot(data=dataset_, x=x_axis, bins=20, kde=True)
            st.balloons()
        elif dv_technique == 'Bar Graph':
            sns.barplot(data=dataset_, x=x_axis, y=y_axis)
            st.balloons()

        st.pyplot(plt)

