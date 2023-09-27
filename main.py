import pandas as pd
import streamlit as st
from define import *

terms_lst = st.text_input("Input terms as a comma separated list: ").split(",")

df = pd.DataFrame(
    {
        "Terms":terms_lst,
        "Definitions":definitions_only(terms_lst)
    }
)

st.write(df)








