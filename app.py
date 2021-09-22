import streamlit as st
import pandas as pd
from data_pull import Logowanie
# ---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(page_title='Facebook Insight API data connector',
                   layout='wide')
# ---------------------------------#
st.sidebar.title("1. Enter your Facebook Developer API credentials:")
app_id = st.sidebar.text_input(label="App ID")
app_secret = st.sidebar.text_input(label="App Secret", type="password")
access_token = st.sidebar.text_input(label="Access Token")
ad_account = st.sidebar.text_input(label="Ad Account")
st.sidebar.button(label="Submit")
st.header("**This application let's you quickly import your ad data from facebook account 😎.**")
if app_id != "" and app_secret != "" and access_token != "" and ad_account != "":
    try:
        credential = Logowanie(app_id, app_secret, access_token, ad_account)
        dane = credential.login()
        df = pd.DataFrame(data=dane)
        st.markdown("Here you can find data frame with your data:")
        st.write(df)
        dane_csv = pd.DataFrame.to_csv(df)
        st.success("Successfully connected to the database!")
        st.download_button(label='Download your data', file_name='dane.csv', data=dane_csv)
    except Exception as ex:
        st.error(ex)






