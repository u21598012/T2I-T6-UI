import streamlit as st
import requests
import json

# Configure the page
st.set_page_config(
    page_title="Health Advice Chatbot",
    page_icon="🏥",
    layout="wide"
)

# API endpoint
API_URL = "http://localhost:5001"

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🏥 Health Advice Chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask for health advice..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Send request to Flask API
            response = requests.post(
                f"{API_URL}/health-advice",
                json={"prompt": prompt},
                timeout=60
            )
            
            if response.status_code == 200:
                bot_response = response.json().get("response", "No response received")
            else:
                error_details = response.json().get("error", "Unknown error")
                bot_response = f"⚠️ Error: {error_details}"
        
        except requests.exceptions.ConnectionError:
            bot_response = "⚠️ Unable to connect to the API. Please make sure the Flask server is running on http://localhost:5001"
        except requests.exceptions.Timeout:
            bot_response = "⚠️ Request timed out. Please try again."
        except Exception as e:
            bot_response = f"⚠️ Error: {str(e)}"
        
        message_placeholder.markdown(bot_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Sidebar with options
with st.sidebar:
    st.header("Settings")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("Connected to: http://localhost:5001/health-advice")
    st.info("💡 This chatbot provides health advice using ARK team agents.")
