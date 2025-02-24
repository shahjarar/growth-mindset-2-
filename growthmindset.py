# streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon= "★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("welcome to your Growth Journey")
st.write("Embrace challenges, learn from mistake, and unlock your potential. This AI-powered app help you build a growth mindset with reflaction,challenges, and achievement!☆")

# quote section
st.header("✌ Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatel: it is the courage to continue that counts.- winston churchill")

st.header(" what's your challenge Today?")
user_input = st.text_input("Describe a challenge you're faceing:")


#condition
if user_input:
    st.sucess( f"💪🏽 you're faceing: {user_input}. keep pusing forward towards your goal!🚀")
else:
    st.warning("Tell  us about your challenge to get started!")

#reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("write your reflections here:")

if reflection:
    st.success(f"🏋️‍♂️Great Insight! your reflection: {reflection}")
else: 
    st.info("Reflecting on past experience help you grow! Share your difficulties")

#acheivements
st.header("🏆♛ Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")

if acheivment: 
    st.success(f"🌹Amazing! you achieved:{acheivment}")
else:
    st.info("Big or small , every acheivement counts! Share one now🍀")


#footer
st.write("- - -")
st.write("🚀keep beliveing in yourself.Growth is a journey, not a destination!💐")
st.write("**🌻Created by Shahjarar***")

