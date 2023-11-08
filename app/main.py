import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json
import datetime

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
    

df = pd.DataFrame([
    {
        'Date': '2022-12-15',
        'Amount': 100.5
    },
    {
        'Date': '2022-12-16',
        'Amount': 120.5
    },

])

df