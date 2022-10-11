import pandas as pd
import streamlit as st
import pickle

item_list=pickle.load(open('item_dict.pkl','rb'))
item_=pd.DataFrame(item_list)

st.title('Food Recommender System')

option = st.selectbox(
    'How would you like to be contacted?',item['item_name'].values )