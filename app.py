import streamlit as st
from src.components.listener import speech_to_text
from src.components.llm_model import Model

if 'can_refresh' not in st.session_state:
    st.session_state['can_refresh']=False

st.set_page_config("MultiLingual AI Assistant")

st.title("Multilingual AI Assistant 🤖")

if st.button("Ask query"):
    with st.spinner("Processing..."):
        query=speech_to_text().get_speech()
        if query!=None:
            st.session_state['can_refresh']=True
            response=Model().generate_response(query)
            st.markdown(body=f"""
            <h1>Question</h1>
            <p>{query}</p>
            <h1>Answer</h1>
            """, unsafe_allow_html=True)
            st.markdown(response,unsafe_allow_html=True)
        else:
            if st.button("Refresh"):
                st.rerun()
            st.write("Please refresh the page")

if st.session_state['can_refresh']:
    if st.button("Refresh"):
        st.session_state['can_refresh']=False
        st.rerun()