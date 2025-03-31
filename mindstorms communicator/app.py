import streamlit as st
import time
from conversation import conversation, patient_responses
from tts import text_to_speech
from state import initialize_state
from styles import app_style

# Initialize state
initialize_state()

# Set up UI
st.title("🧠 Mindstorms Companion")
st.write("_Carer is interacting with the patient using BCI technology._")

# Apply styles
st.markdown(app_style, unsafe_allow_html=True)

# Restart Button
if st.button("🔁 Restart Conversation"):
    st.session_state.current_step = 0
    st.session_state.audio_html = []
    st.session_state.step_completed = False
    st.rerun()

# Display conversation
for i in range(len(st.session_state.audio_html)):
    st.markdown(f'<div class="chat-message"><strong>Carer:</strong> {conversation[i]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-message"><strong>Patient:</strong> {patient_responses[i]}</div>', unsafe_allow_html=True)

# Handle interaction step by step
if st.session_state.current_step < len(conversation):
    index = st.session_state.current_step
    question = conversation[index]
    response = patient_responses[index]

    if not st.session_state.step_completed:
        # Carer asks
        st.markdown(f'<div class="chat-message"><strong>Carer:</strong> {question}</div>', unsafe_allow_html=True)
        q_audio = text_to_speech(question, tld="co.za", slow=False)
        st.markdown(q_audio, unsafe_allow_html=True)
        time.sleep(3)

        # Simulate BCI processing
        st.markdown('<div class="processing">🧠 Processing ...</div>', unsafe_allow_html=True)
        time.sleep(5)

        # Patient responds
        st.markdown(f'<div class="chat-message"><strong>Patient:</strong> {response}</div>', unsafe_allow_html=True)
        r_audio = text_to_speech(response, tld="co.uk", slow=True)
        st.markdown(r_audio, unsafe_allow_html=True)
        time.sleep(3)

        # Store and move on
        st.session_state.audio_html.append((q_audio, r_audio))
        st.session_state.step_completed = True
        st.rerun()

    else:
        # Step is done, move to next one
        st.session_state.step_completed = False
        st.session_state.current_step += 1
        st.rerun()

# End of chat
else:
    st.balloons()
    st.write("🎉 Conversation complete! The carer has received the patient's responses.")
