import streamlit as st
from transformers.inference_engine import TransformerInferenceEngine

st.set_page_config(layout="wide")

st.title("Amharic Linguistic AI Platform")

engine = TransformerInferenceEngine()

sentence = st.text_input(
    "Sentence",
    "አብይ አህመድ በአዲስ አበባ ንግግር አደረጉ"
)

if sentence:

    result = engine.predict(sentence)

    st.json(result)