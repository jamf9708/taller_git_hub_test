import streamlit as st
import src.EDA as eda
import src.images as img
import src.plots as plot

st.set_option('deprecation.showPyplotGlobalUse', False)

#Title
st.title("El mejor taller de GitHub")
st.header("I knowwww!")

eda.read_dataset()
eda.show_dataset()
eda.show_dataset_2()
eda.select_column()
plot.read_dataset()
plot.plots()
plot.groupbys()
img.images()
