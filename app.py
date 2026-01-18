import streamlit as st
from query_data import query_rag

# --- 1. Basic Page Setup ---
st.set_page_config(page_title="Simple AI Assistant", page_icon="💬")
st.title("💬 AI Assistant")

# --- 2. Initialize Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. Display Chat Messages from History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 4. User Input Logic ---
if prompt := st.chat_input("How can I help you?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call your RAG logic
                response = query_rag(prompt)
                st.markdown(response)
                
                # Add assistant response to history
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {e}")