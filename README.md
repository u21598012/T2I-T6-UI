# Chatbot Streamlit UI

A simple Streamlit-based chat interface that connects to a Flask API backend.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure your Flask API is running on http://localhost:5001

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## API Requirements

The Flask API should have a `/chat` endpoint that accepts POST requests with the following format:

**Request:**
```json
{
  "message": "user message here"
}
```

**Response:**
```json
{
  "response": "bot response here"
}
```

## Features

- Clean chat interface
- Message history
- Clear chat button
- Error handling for API connection issues
