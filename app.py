import streamlit as st
from datetime import date

st.set_page_config(page_title="❤️ Convite Especial ❤️")

if "aceitou" not in st.session_state:
    st.session_state.aceitou = False

if not st.session_state.aceitou:

    st.title("❤️ Tenho uma pergunta para você ❤️")
    st.subheader("Camila quer sair comigo???")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sim ❤️"):
            st.session_state.aceitou = True
            st.rerun()

    with col2:
        if st.button("Claro 😍"):
            st.session_state.aceitou = True
            st.rerun()

else:

    st.balloons()

    st.title("🥰 Que felicidade!")

    st.write("Agora escolha a data do nosso encontro ❤️")

    data = st.date_input(
        "Escolha a data",
        min_value=date.today()
    )

    st.success(
        f"Nosso encontro será em {data.strftime('%d/%m/%Y')} ❤️✨"
    )

    st.markdown(
        "### Mal posso esperar para te ver 💖"
    )
