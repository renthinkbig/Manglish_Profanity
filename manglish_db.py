import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
import base64

# Load Google Sheets API credentials
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
st.write("Secrets Loaded:", st.secrets)
#CREDS = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=SCOPE)

# Connect to Google Sheets
# client = gspread.authorize(CREDS)
# SHEET_NAME = "manglish_dataset"  # Change this to your sheet's name
# sheet = client.open(SHEET_NAME).sheet1  # Open first sheet
def sidebar_bg(side_bg):

   main_bg_ext = 'jpg'

   st.markdown(
       f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
                background-size: cover
            }},
            </style>
            """,
       unsafe_allow_html=True
   )


if __name__ == "__main__":
    side_bg = 'bckg1.jpg'
    sidebar_bg(side_bg)
    text='''📢 Calling All Malayalam Speakers! 🚀  

We are conducting an academic research study on the usage of Manglish abuse words 
like **PODA PATTI**, **MY**#**🤬.

We need your **help!!!!**

👉 What do we need?  
A list of Manglish bad words/slang/unparliamentary/abuse phrases that you come across in comments.  

👉 Why?  
This research aims to analyze language patterns and their role in informal communication.  

🔒 Privacy Assurance:  
✅ No personal data is collected—only words and phrases for linguistic analysis.  

Your input will help us to develop linguistic models. \n
**Thank you!** '''
    st.sidebar.image('logo.jpg',width=400)
    with st.sidebar:
            st.write(f'''{text}''')
    st.title("Manglish Profanity Dataset Builder")

    # Display stored data
    # data = sheet.get_all_records()
    # df = pd.DataFrame(data)

    # Initialize session state for input field if not exists
    if "new_entry" not in st.session_state:
        st.session_state.new_entry = ""

    # User input to add new data
    new_entry = st.text_input("Enter new data:", st.session_state.new_entry)
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Submit",type="primary"):
            if new_entry:
                # sheet.append_row([new_entry])
                st.success("Data added successfully! Thank you for your response.")


