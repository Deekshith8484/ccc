import streamlit as st

def initialize_state():
    if "current_step" not in st.session_state:
        st.session_state.current_step = 0
    if "audio_html" not in st.session_state:
        st.session_state.audio_html = []
    if "step_completed" not in st.session_state:
        st.session_state.step_completed = False
