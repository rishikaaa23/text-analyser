import streamlit as st
from textblob import TextBlob

st.title('Text Analyser')

user_text=st.text_area("enter your text here")

if st.button("Analyse Sentiment"):
    blob=TextBlob(user_text)
    polarity=blob.sentiment.polarity
    subjectivity=blob.sentiment.subjectivity

    if polarity>0:
        st.success("text is positive")
    elif polarity<0:
        st.error("text is negative")
    elif polarity==0:
        st.warning("text is neutral")

    if subjectivity==0:
        st.success("its a fact")
    else:
        st.warning("its an opinion")