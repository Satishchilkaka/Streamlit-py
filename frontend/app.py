import streamlit as st
col1, col2, col3 = st.columns([1,2,1])
col1.markdown("My app name")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
