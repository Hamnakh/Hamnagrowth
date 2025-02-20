#streamlit
import streamlit as st


# import pandas as pd 
# import os 
# from  io import BytesIO

st.set_page_config(page_title= "growth mindset proect", prorct_icons='★')
st.title("Growth mindset challenge: web app with streamlit")


st.header("Welcome to your growth journey!")
st.write("Embrace challeenges, learn from mistakes, and unlock our full potential. This AI-powered app helps you build a growth mindset with reflectio, challenges, and achievements!✪")

#quote section
st.header("Today's Growth Mindset Quote")
st.write(""🏆Success is not final, failure is not fatal: it is the courage to continue that counts."- winston Churchill")

st.header("What's your challenge today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f"you're facing: {user_input}. keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!") 



#reflexing
st.header("Reflect on your learning")
reflection = st.text_area("write your reflctions here:")

if reflection:
    st.Success(f"Great Insight! your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! share your difficulties")


#acheivements
st.header("Celebrate your wins!") 
acheivement = st.text_input("Share something you're recently accomplised:")   

if acheivement:
    st.success(f"🌟 Amazing! you achieved: {acheivement}")
else:
    st.info("Big or small, every achievement counts! share one now 😍")


#footer
st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination! ✨")
st.write("⛔ Create by Hamna***")



































#custom css
st.markdown(
    """
    <style>
    .stApp{
        background-color: black;
        color: white;
         }
         </style>
         """,
         unsafe_allow_html=True
)

#title and description
st.title("Datasweeper sterling integrator by Hamna")
st.write("Transform your files between csv and excel formats with built-in data cleaning and visualization creating the project for quarter 3!")


#file uploader 
uploaded_files = st.uploader("upload your files (accepts csv or excel):",type=["csv", "xlsx"], accept_multiple_files=(True))

if uploaded_files:
    for file in uploaded_files:
        


       
file_ext = os.path.splitext (file.name)[-1].lower()

if file_ext == ".csv":
df = pd_read_csv(file)
elif file_ext == "xlsx" :
df = pd.read_excel(file)

else:
st.error(f"unsupported  file type: {file_ext}")
continue

#file data
st.write("preview the head of the Dataframe")
st.dataframe (df.head())

#data cleaning option
st.subheader("Data cleaning options")
if st.checkbox (f"clean data for {file.name}"):
col1,col2 = st.columns(2)

with col1:
if st.button(f"Remote duplicates from the file: df.drop_duplicates(inplace=True)")
st.write("✅Duplicates removed !")

with col2:
if st.button(f"fill missing values for {file.name}"):
numeric_cols=df.select_dtypes(includes=['number']).columns
df[numeric.cols]=df[numeric_cols].fillna (df[numeric_cols].means)
st.write("✅Missing vslues have been filled!")
st.subheaders("select columns to keep")