import streamlit as st
import time

# Title
st.title("🎂 Birthday Month Guesser!")

# Instructions
st.write("Answer a few fun questions and I will guess your birthday month!")

# Name input
name = st.text_input("What is your first name?").lower()

if name:
    st.write(f"Hello, {name}!!!")
    time.sleep(1)

    # Other fun questions
    color = st.text_input("What is your favorite color?")
    animal = st.text_input("What is your favorite animal?")
    season = st.selectbox("What is your favorite season?", ["Spring", "Summer", "Fall", "Winter"])
    year = st.number_input("What year were you born?", min_value=1900, max_value=2025, step=1)
    snow = st.radio("Was there snow on the ground when you were born?", ["Yes", "No"])

    # Only show the “Thinking” sequence after they type their name
    if st.button("Guess My Birthday Month"):
        placeholder = st.empty()  # placeholder to update text

        placeholder.text("Thinking...")
        time.sleep(2)
        placeholder.text("I will now guess your birthday month!")
        time.sleep(2)
        placeholder.text("Thinking...")
        time.sleep(3)
        placeholder.text("Thinking harder...")
        time.sleep(3)
        placeholder.text("Your birthday month is...")
        time.sleep(2)

        # Determine the birthday month based on name
        if name == "aayla":
            month = "November!!! 🎉"
        elif name == "erica":
            month = "May!!! 🎉"
        elif name == "flynn":
            month = "May!!! 🎉"
        else:
            month = "I can't guess your birthday month 😅"

        st.success(month)
