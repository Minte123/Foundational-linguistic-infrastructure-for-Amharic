import streamlit as st
import json
from pathlib import Path

POS_TAGS = ["NOUN", "VERB", "ADJ", "ADV", "PROPN"]
NER_TAGS = ["PER", "LOC", "ORG", "DATE", "O"]

st.set_page_config(page_title="Amharic Annotation Tool")

st.title("Amharic AI Annotation Infrastructure")

sentence = st.text_input(
    "Enter Amharic sentence",
    "አብይ አህመድ ዛሬ ንግግር አደረጉ"
)

if "annotations" not in st.session_state:
    st.session_state.annotations = {}

tokens = sentence.split()

active_pos = st.radio("POS Tag", POS_TAGS)
active_ner = st.radio("NER Tag", NER_TAGS)

cols = st.columns(len(tokens))

for idx, token in enumerate(tokens):
    label = token

    if idx in st.session_state.annotations:
        pos, ner = st.session_state.annotations[idx]
        label = f"{token}\n{pos}/{ner}"

    if cols[idx].button(label, key=f"token_{idx}"):
        st.session_state.annotations[idx] = (active_pos, active_ner)

if st.button("Save Annotation"):
    output = {
        "sentence": sentence,
        "tokens": []
    }

    for idx, token in enumerate(tokens):
        pos, ner = st.session_state.annotations.get(idx, ("", ""))

        output["tokens"].append({
            "word": token,
            "pos": pos,
            "ner": ner
        })

    data_path = Path("phase1_annotation_ui/data")
    data_path.mkdir(parents=True, exist_ok=True)

    with open(data_path / "annotations.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(output, ensure_ascii=False) + "\n")

    st.success("Annotation saved.")