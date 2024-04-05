import streamlit as st
from groq import Groq

GROQ_API_KEY = "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"

client = Groq(
    api_key = GROQ_API_KEY,
)

query = st.text_input("Input here", placeholder = "Ask me!")

if query:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="mixtral-8x7b-32768",
    )

    response = chat_completion.choices[0].message.content

    st.markdown(":blue[Query:]")
    st.markdown(query)
    st.markdown(":green[Response: ]")
    st.markdown(response)
