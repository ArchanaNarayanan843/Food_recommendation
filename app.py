import streamlit as st
import pickle
import pandas as pd

def recommend(food):
    item_index = item[item['item_name'] == food].index[0]
    distance = similarity[item_index]
    item_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])
    listitem = []
    pictures=[]
    count = 0
    #recommended_items=[]
    for i in item_list:

        item_id = i[0]
        #fetch_image from api

        if item.iloc[i[0]].item_name not in listitem:
            listitem.append(item.iloc[i[0]].item_name)
            pictures.append(img[img['item_name']==item.iloc[i[0]].item_name]['images'].values[0])
            #pictures.append(img[img['name']==item.iloc[i[0]].item_name]['image'].values[0])
            count += 1
            if count == 6:
                break

    #return recommended_items
    return listitem,pictures

item_dict = pickle.load(open('item_dict.pkl','rb'))
item=pd.DataFrame(item_dict)

option=pickle.load(open('dict_item.pkl','rb'))
opt=pd.DataFrame(option)

image=pickle.load(open('image.pkl','rb'))
img=pd.DataFrame(image)

similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Food Recommender System')

selected_item_name=st.selectbox(
'Which item do you prefer?',
opt['item_name'].values)

if st.button('Recommend'):
    names,pictures = recommend(selected_item_name)
    number=0

    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
            st.text(names[1])
            st.image(pictures[1])
    with col2:
            st.text(names[2])
            st.image(pictures[2])
    with col3:
            st.text(names[3])
            st.image(pictures[3])

    with col4:
            st.text(names[4])
            st.image(pictures[4])

    with col5:
            st.text(names[5])
            st.image(pictures[5])
