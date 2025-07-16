"""Streamlit tabanlı kullanıcı dostu arayüz."""

import streamlit as st

from src.retrieve import retrieve_answer


st.set_page_config(page_title="İş Hukuku Danışman", page_icon="⚖️")
st.title("Türk İş Hukuku Danışmanlık Botu")

st.sidebar.header("Nasıl Kullanılır?")
st.sidebar.markdown(
    "Sorunuzu aşağıdaki alana yazıp **Gönder** butonuna basın.\n"
    "Belge koleksiyonunu güncellemek için `src/ingest.py` çalıştırılabilir."
)

if "history" not in st.session_state:
    st.session_state.history = []

for role, text in st.session_state.history:
    with st.chat_message(role):
        st.markdown(text)

prompt = st.chat_input("Sorunuzu yazın")
if prompt:
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    answer = retrieve_answer(prompt)
    st.session_state.history.append(("assistant", answer))
    with st.chat_message("assistant"):
        st.markdown(answer)
