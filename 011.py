import streamlit as st
with st.form('Order do uong'):
    drinks = ('cà phê', 'trà', 'sinh tố', 'nước ép', 'nước giải khát' ,'đồ uống truyền thống')
    option_drinks = st.selectbox('Ban muon uong do uong nao?',drinks)
    sugars = ('cane sugar', 'brown sugar', 'confectioners sugar', 'honey', 'maple syrup')
    option_sugar = st.selectbox('Ban muon loai duong nao?', sugars)
    topping = ('lychee', 'coconut', 'grass', 'aloe vera')
    option_top = st.selectbox('Ban muon them topping nao?', topping)
    num = st.slider('So luong ban muon dat',1,50,2)
    bill = {'Loai do uong:': option_drinks,'Loai duong:': option_sugar,'Loai topping:': option_top,'So luong:':num }
    submitted = st.form_submit_button('Xac nhan')
    if submitted:
        st.write('Ban da chon:')
        for x,y in bill.items():
            st.write(x,y)