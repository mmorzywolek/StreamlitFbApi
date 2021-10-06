import streamlit as st
import pandas as pd
from data_pull import Logowanie

# ---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(page_title='Facebook Insight API data connector',
                   layout='wide')
# ---------------------------------#
option = st.sidebar.selectbox("Select what you want to do?",
                              ('Read the data', 'Make the dashboard', 'Explore the data', 'Model your data'), 0)

st.header(option)

if option == 'Read the data':
    st.sidebar.subheader("1. Enter your Facebook Developer API credentials:")
    app_id = st.sidebar.text_input(label="App ID")
    app_secret = st.sidebar.text_input(label="App Secret", type="password")
    access_token = st.sidebar.text_input(label="Access Token")
    ad_account = st.sidebar.text_input(label="Ad Account")
    st.sidebar.subheader('2. Specify your data')
    # Sidebar Options:
    level = st.sidebar.selectbox('Level', ('ad', 'adset', 'campaign', 'account'))
    date_preset = st.sidebar.selectbox('Period', ('last_7d', 'last_14d', 'last_28d', 'last_30d', 'last_90d'))
    breakdowns = st.sidebar.selectbox('Breakdowns', ('region', 'gender', 'age', 'age, gender'))
    st.header("**This application let's you quickly import your ad data from facebook account 😎.**")
    st.sidebar.button(label="Submit")
    if st.sidebar.button:
        try:
            credential = Logowanie(app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns)
            dane = credential.login()
            df = pd.DataFrame(data=dane)
            st.markdown("Here you can find data frame with your data:")
            st.dataframe(df)
            dane_csv = pd.DataFrame.to_csv(df)
            st.success("Successfully connected to the database!")
            st.download_button(label='Download your data', file_name='dane.csv', data=dane_csv)
        except Exception as ex:
            st.error(ex)

if option == 'Make the dashboard':
    st.sidebar.header("2. Choose your variables")

if option == 'Explore the data':
    st.sidebar.header("3. Make your exploratory analysis")

if option == 'Model your data':
    st.sidebar.header("4. Predict your ads performance")
