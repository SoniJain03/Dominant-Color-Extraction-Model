import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


st.title("Dominant Color Extraction")

st.subheader("Upload image")
img=st.file_uploader("Choose image")
if img is not None:
    st.header("Original image")
    st.image(img)

    #Kmeans code

    img=plt.imread(img)
    n=img.shape[0]*img.shape[1]
    all_pixels=img.reshape((n,3))

    model=KMeans(n_clusters=3)
    model.fit(all_pixels)

    centers=model.cluster_centers_.astype("uint8")
    new_img=np.zeros((n,3),dtype="uint8")
    for i in range(n):
        group_idx=model.labels_[i]
        new_img[i]=centers[group_idx]
    new_img = new_img.reshape((img.shape[0], img.shape[1], 3))


    st.header("Modified image")
    st.image(new_img)

