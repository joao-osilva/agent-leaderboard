import streamlit as st
from tasks import print_json
from redis_db import run_task

st.title("Submit a new agent")
st.write(
    "tbd"
)

if st.button('Start Long Task'):
    run_task(print_json)