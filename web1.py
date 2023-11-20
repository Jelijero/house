import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import pickle

html_temp = """
<div style="background-color:cyan;padding:1.5px">
<h1 style="color:black;text-align:center;">House Price Prediction</h1>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)


st.write("\n\n"*2)
filename="house"
model = pickle.load(open(filename, 'rb'))


st.subheader('HOUSE SPECIFICATIONS')


guestroom=st.radio("Guestroom",("Yes","No"))
basement=st.radio("Basement",("Yes","No"))
bedrooms= st.number_input("Bedrooms:",min_value=1, max_value=6, value=1)
bathrooms= st.number_input("Bathrooms:",min_value=1, max_value=4, value=1)
area=st.slider("Area",min_value=1650,max_value=16200,value=1650)
if (guestroom=="Yes"):
    guestroom=1
else:
    guestroom=0
if (basement=="Yes"):
    basement=1
else:
    basement=0




my_dict = {"area":area, "bedrooms":bedrooms,"bathrooms":bathrooms,  "guestroom":guestroom, "basement":basement}
df = pd.DataFrame.from_dict([my_dict])




df_show = df.copy()

st.table(df_show)


if st.button("Predict"):
    pred = model.predict(df)
    for i in pred:
        amt=i

    st.write("The estimated House price :",amt)
