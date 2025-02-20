import streamlit as st


st.set_page_config(page_title= "growth mindset proect", page_icon='★')
st.title("Growth mindset challenge: web app with streamlit")


st.header("Welcome to your growth journey!")
st.write("Embrace challeenges, learn from mistakes, and unlock our full potential. This AI-powered app helps you build a growth mindset with reflectio, challenges, and achievements!✪")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("🏆Success is not final, failure is not fatal: it is the courage to continue that counts."+"- winston Churchill")

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
    st.success(f"Great Insight! your reflection: {reflection}")
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



































