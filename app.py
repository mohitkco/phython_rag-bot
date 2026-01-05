import streamlit as st
from query_data import query_rag

# --- UI Setup ---
# This changes the browser tab name
st.set_page_config(page_title="AI Assistant", page_icon="💬")

# Clean Title
st.title("💬 Personal AI Assistant")
st.markdown("Ask a query below to get started.")

# --- Initialize Session History ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Conversation ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Interaction ---
# Changed "How do I play..." to a neutral "Ask a query..."
if prompt := st.chat_input("Ask a query..."):
    # Add user message to UI and history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Processing your query..."):
            try:
                # Calls your logic from query_data.py
                response = query_rag(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {e}")