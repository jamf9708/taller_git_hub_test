import streamlit as st
import os
from PIL import Image, ImageEnhance

# Images
@st.cache
def load_image(img):
    im = Image.open(os.path.join(img))
    return im

def images():
    species_type = st.radio("Select Species Type", ("Iris-setosa", "Iris-virginica", "Iris-versicolor"))
    if species_type == "Iris-setosa":
        st.text("Showing Setosa Species")
        st.image(load_image('imgs/iris_setosa.jpg'))
    elif species_type == "Iris-virginica":
        st.text("Showing Virginica Species")
        st.image(load_image('imgs/iris_virginica.jpg'))
    else:
        st.text("Showing Versicolor Species")
        st.image(load_image('imgs/iris_versicolor.jpg'))
        
    if st.checkbox("Show/Hide Image"):
        my_image = load_image ("imgs/iris_setosa2.jpg")
        enh = ImageEnhance.Contrast(my_image)
        num = st.slider("Set Image Contrast", 1.0, 4.0)
        img_width = st.slider("Set Image Width", 300, 500)
        st.image(enh.enhance(num), width=img_width)
        
    if st.button("About App"):
        st.text("Iris EDA App")
        st.text("Built with Streamlit")
        st.text("Cudos to the Streamlit Team")
