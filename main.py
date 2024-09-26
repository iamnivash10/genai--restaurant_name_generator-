import  streamlit as st
import  langchainhelp
st.title("restaurant_name_generator")
cuis_name = st.sidebar.selectbox("pick a cuisine",("indian","chinese","mexican","italian","american",))

if cuis_name:
    res = langchainhelp.gen_res_name_and_menu(cuis_name)
    st.header(res['resturant_name'])
    menu_items = res['menu'].split(',')
    for item in menu_items:
        st.write("-",item)


