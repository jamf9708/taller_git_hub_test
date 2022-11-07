import streamlit as st
import pandas as pd
import os 

# EDA
#Funt. to Load Dataset
@st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv(os.path.join(dataset), index_col=0)
    return df

def read_dataset():
    global data
    my_dataset = './data/iris.csv'
    data = explore_data(my_dataset)

def select_column():
    # Select A Column
    col_option = st.selectbox("Select Column", ("SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"))
    if col_option == "SepalLengthCm":
        st.write(data["SepalLengthCm"])
        #st.write(type(data["SepalLengthCm"]))
    elif col_option == "SepalWidthCm":
        st.write(data[["SepalWidthCm"]])
        #st.write(type(data[["SepalWidthCm"]]))
    elif col_option == "PetalLengthCm":
        st.write(data[["PetalLengthCm"]])
    elif col_option == "PetalWidthCm":
        st.write(data[["PetalWidthCm"]])    
    elif col_option == "Species":
        st.write(data[["Species"]])
    else:
        st.write("Select a Column") 
