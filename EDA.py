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

def show_dataset():
    if st.checkbox("Preview Dataset"):    
        if st.button("Head"):
            st.write(data.head())
        elif st.button("Tail"):
            st.write(data.tail())
        else:
            st.write(data.head(2))
            
def show_dataset_2():
    # Show entire dataset
    if st.checkbox("Show All Dataset"):
        #st.write(data)
        st.dataframe(data)
        
    # Show Column Name
    if st.checkbox("Show Column Names"):
        st.write(data.columns)

    # Show Dimensions
    data_dim = st.radio("What Dimensions Do You Want to See?", ("Rows", "Columns", "All"))
    if data_dim == "Rows":
        st.text("Showing Rows")
        st.write(data.shape[0])
    elif data_dim == "Columns":
        st.text("Showing Columns")
        st.write(data.shape[1])
    else:
        st.text("Showing Shape of dataset")
        st.write(data.shape)
        

    # Show Summary
    if st.checkbox("Show Summary of Dataset"):
        st.write(data.describe())
