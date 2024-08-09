import streamlit as st
import hindi, english, maths
from PIL import Image

favicon = Image.open("img/maths_logo.png")
# Set the page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=favicon,
    layout="wide"
)


c1, c2 = st.columns(2)
with c1:
    c1.image('img/Education-Logo.jpg', width=200)

with c2:
    c2.markdown("<h1 style='text-align: center; color:#7C129D;'>WELCOME TO Stream App !<h1>", unsafe_allow_html=True)


options = ['Hindi', 'English', 'Maths']

selected_option = st.selectbox('Select Option', options=options)

if selected_option == 'Hindi':
    hindi.hindiPoem()

elif selected_option == 'English':
    english.EnglishPoem()

else:
    c1, c2, c3 = st.columns(3)
    with c2:
        c2.image('img/maths_logo.png', width=150)
    n1 = st.number_input("Enter First Number..")
    n2 = st.number_input("Enter second Number...")
    if st.button("Add"):
        maths.add(n1, n2)
