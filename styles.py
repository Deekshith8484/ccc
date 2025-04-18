app_style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        background-color: #c2e2f5;
        color: #545454;
    }

    /* Override the Streamlit title styling directly */
    h1 {
        color: #0f27f7;
        background-color: #ff66c4;
        padding: 0.5rem;
        border-radius: 10px;
        text-align: center;
    }

    /* Chat messages for Carer and Patient */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .chat-message {
        display: flex;
        align-items: center;
        max-width: 80%;
        padding: 10px;
        border-radius: 10px;
        font-size: 18px;
        color: white;
        background: linear-gradient(135deg, #01d9fe, #0788fe, #8c66ff, #e946fe);
        background-size: 400% 400%;
        animation: flowColors 10s ease infinite;
    }

    .chat-message strong {
        color: #ffffff;
        margin-right: 6px;
    }

    .processing {
        align-self: center;
        font-style: italic;
        color: #0788fe;
        background: none;
    }

    .stButton>button {
        background-color: #ff66c4;
        color: white;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 10px;
        font-weight: bold;
        transition: background 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #e946fe;
        color: white;
    }

    a {
        color: #01d9fe;
    }

    a:hover {
        color: #e946fe;
    }

    @keyframes flowColors {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
"""
