import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

#Funt. to Load Dataset
@st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv(os.path.join(dataset), index_col=0)
    return df
def read_dataset():
    global data
    my_dataset = './data/iris.csv'
    data = explore_data(my_dataset)
    
def plots():
    global data
    my_dataset = './data/iris.csv'
    data = explore_data(my_dataset)
    #Plot
    if st.checkbox("Show Bar Plot with Matplotlib"):
        st.write(data.plot.bar() )
        st.pyplot()
        
    #Correlation
    if st.checkbox("Show Correlation Matrix with Matplotlib"):
        plt.matshow(data.corr())
        st.pyplot()
        
    #Correlation
    if st.checkbox("Show Correlation Matrix with Seaborn"):
        st.write(sns.heatmap(data.corr()))
        st.pyplot()

def groupbys():    
    v_group = data.groupby("Species").sum()   
    # Group
    if st.checkbox("Show Bar Chart Plot"):   
        st.bar_chart(v_group)
        
    # Group
    if st.checkbox("Show Line Chart Plot"):
        st.line_chart(data)
        
    # Group
    if st.checkbox("Show Area Chart Plot"):
        st.area_chart(v_group)

