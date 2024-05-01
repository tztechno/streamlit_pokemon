import streamlit as st
import os
import random

dir0 = './pokemon_jpg'
paths=[]
for file in os.listdir(dir0):
    paths+=[os.path.join(dir0,file)]

def shuffle_images(paths):
    random.shuffle(paths)
    return paths

st.title("Pokemon 9")

if st.button("Shuffle"):
    shuffled_paths = shuffle_images(paths)
    for i in range(3):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(shuffled_paths[i], use_column_width=True)
        with col2:
            st.image(shuffled_paths[i+3], use_column_width=True)
        with col3:
            st.image(shuffled_paths[i+6], use_column_width=True)
