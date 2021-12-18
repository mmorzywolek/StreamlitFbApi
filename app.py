from datetime import datetime
import streamlit as st
import pandas as pd
from data_pull import Logowanie
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_apex_charts import line_chart, bar_chart, create_chart_data
from st_card import st_card


today = datetime.today()
# ---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(page_title='Facebook Insight API data connector',
                   layout='wide')
# ---------------------------------#
option = st.sidebar.selectbox("Select what you want to do?",
                              ('Read the data', 'Make the dashboard', 'Explore the data', 'Model your data'), 0)
#Fixed sidebar with API credentials
st.header(option)
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

@st.cache
def get_connection():
    return app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns


if option == 'Read the data':
    st.header("**This application let's you quickly import your ad data from your facebook ad account 😎.**")
    if st.sidebar.button(label="Submit"):
        if app_id != "" and app_secret != "" and access_token != "" and ad_account != "":
            try:
                app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns = get_connection()
                credential = Logowanie(app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns)
                dane = credential.login()
                df = pd.DataFrame(data=dane)
                st.markdown("Here you can find data frame with your data:")
                st.dataframe(df)
                dane_csv = pd.DataFrame.to_csv(df)
                st.success("Successfully connected to your Facebook ad account!")
                st.download_button(label='Download your data', file_name=f'{today}_fb_data.csv', data=dane_csv)
            except Exception as ex:
                st.error(ex)
# 1. Connect trough fixed credentials 2. Using same query create EDApip
if option == 'Make the dashboard':
    st.sidebar.header("2. Choose your variables")
    if app_id != "" and app_secret != "" and access_token != "" and ad_account != "":
        try:
            app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns = get_connection()
            credential = Logowanie(app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns)
            dane = credential.login()
            df = pd.DataFrame(data=dane)
            df1 = df[['clicks']]
            filtered = df[['clicks', 'reach', 'spend']]
            filtered[["clicks", "reach", "spend"]] = filtered[["clicks", "reach", "spend"]].apply(pd.to_numeric)
            line_chart("Line Chart", df1)
            sum1 = int(filtered["clicks"].sum())
            sum2 = int(filtered["spend"].sum())
            sum3 = int(filtered["reach"].sum())
            kpi1, kpi2, kpi3 = st.columns(3)

            with kpi1:
                st.markdown("**Clicks**")
                number1 = st_card('Clicks', value=sum1)

            with kpi2:
                st.markdown("**Spend**")
                number2 = st_card('Spend', value=sum2, unit='PLN', show_progress=True)

            with kpi3:
                st.markdown("**Reach**")
                number3 = st_card('Reach', value=sum3, delta=1, delta_description=f"Total reach for {date_preset}")
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
        except Exception as ex:
            st.error(ex)

if option == 'Explore the data':
    st.sidebar.header("3. Make your exploratory analysis")
    st.header("**This section let's you automatically make some exploratory analysis of your data 😎.**")
    if st.sidebar.button(label="Let's analyze!"):
        if app_id != "" and app_secret != "" and access_token != "" and ad_account != "":
            try:
                app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns = get_connection()
                credential = Logowanie(app_id, app_secret, access_token, ad_account, level, date_preset, breakdowns)
                dane = credential.login()
                df = pd.DataFrame(data=dane)
                pr = ProfileReport(df, explorative=True)
                st.header('**Input DataFrame**')
                st.write(df)
                st.write('---')
                st.header('**Pandas Profiling Report**')
                st_profile_report(pr)
            except Exception as ex:
                st.error(ex)

if option == 'Model your data':
    st.sidebar.header("4. Predict your ads performance")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
