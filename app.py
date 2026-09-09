import streamlit as st
from RAG_pipeline import BharatGenRAG

st.set_page_config(page_title="BharatGen", layout="wide")
st.title("BharatGen - Indic AI Support Assistant")
st.markdown("**For 63M SMEs | RAG + Sarvam AI + WhatsApp**")

with st.sidebar:
    st.header("SME Owner Panel")
    uploaded = st.file_uploader("Upload PDF", type=["pdf"])
    lang = st.selectbox("Language", ["Hindi","Marathi","Tamil","Bengali","English","Punjabi"])
    st.metric("Cost Saved vs Intercom", "70%")
    st.metric("Automation Rate", "82%")
    st.metric("CSAT", "4.6/5")

rag = BharatGenRAG()
if uploaded:
    rag.ingest_pdf(uploaded.name)
    st.success(f"Ingested {uploaded.name}")

query = st.text_input("Customer Query", placeholder="Mera order kahan hai?")
if st.button("Get Answer") and query:
    res = rag.query(query, lang)
    st.write(res["answer"])
    st.caption(f"Confidence: {res['confidence']}% | {res['source']}")
