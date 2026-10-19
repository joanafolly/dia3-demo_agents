import streamlit as st
from llm_agent import ask_llm

st.set_page_config(page_title="Jarvis")
st.title("Barbe-Quasar")

# 1. Créer la mémoire (une seule fois)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bouton pour effacer la mémoire
with st.sidebar:
    if st.button("Nouvelle conversation"):
        st.session_state.messages = []
        st.rerun()

# 2. Réafficher toute la conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Que veux tu moussaillon ?")

if user_input:
    # 3. Garder et afficher la question
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 4. Envoyer toute la conversation au LLM
    with st.chat_message("assistant"):
        response = ask_llm(st.session_state.messages)
        st.markdown(response)

    # 5. Garder la réponse
    st.session_state.messages.append({"role": "assistant", "content": response})