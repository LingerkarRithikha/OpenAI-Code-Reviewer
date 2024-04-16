from openai import OpenAI 
import streamlit as st 

f = open("keys\openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)
st.title("✨GenAI App - AI Code Reviewer ✨")
prompt = st.text_area("Enter your code here for review:")
if st.button("Generate")==True:
    st.snow()
    response = client.chat.completions.create(
                 model="gpt-3.5-turbo-0301",
                 messages=[
                 {"role": "system", "content": """Your are a code debugging assistant. Your task is to help users identify and fix errors in the prompt.
                                                    provide a helpful message above the error and bedug the code. """},
                 {"role": "user", "content": prompt}
                 ]
    )
    st.write("Result:")
    st.write(response.choices[0].message.content)
