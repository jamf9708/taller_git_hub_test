import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

#Funt. to Load Datasettttttttttttttttttttttttttttttttt
@st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv(os.path.join(dataset), index_col=0)
    return df
def read_dataset():
    global data
    my_dataset = './data/iris.csv'
    data = explore_data(my_dataset)
    
