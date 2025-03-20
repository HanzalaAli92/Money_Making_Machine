import streamlit as st
import random
import time
import requests

# 🎯 App Title
st.set_page_config(page_title="💰 Money Making Machine", page_icon="💵", layout="centered")
st.title("💰 Money Making Machine 🚀")

# 📌 Function to generate random money
def generate_money():
    return random.randint(10, 5000)  # Increased money range for fun

# 🎲 Function to get side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get("https://simple-apis-one.vercel.app/side_hustles")
        if response.status_code == 200:
            return response.json()["side_hustle"]
        else:
            return "🚀 Start Freelancing Today!"
    except:
        return "⚠️ Couldn't fetch side hustle. Try again later!"

# 💬 Function to get money-related quotes
def fetch_money_quote():
    try:
        response = requests.get("https://simple-apis-one.vercel.app/money_quotes")
        if response.status_code == 200:
            return response.json()["money_quote"]
        else:
            return "💡 Money is a great servant but a bad master!"
    except:
        return "⚠️ Couldn't fetch quote. Try again later!"

# 💵 Section: Instant Cash Generator
st.markdown("### 💸 Instant Cash Generator")
st.write("Click below to generate some instant virtual cash! 🤑")

if st.button("🤑 Generate Money"):
    with st.spinner("💰 Counting your money..."):
        time.sleep(3)  # Simulating delay
        amount = generate_money()
    st.success(f"🎉 You just made **${amount}**! Go invest it wisely! 🚀")

st.markdown("---")  # Separator

# 🚀 Section: Side Hustle Ideas
st.markdown("### 🚀 Side Hustle Ideas")
st.write("Need an extra income source? Get a cool side hustle idea! 💼")

if st.button("💡 Generate Hustle Idea"):
    with st.spinner("🧐 Finding the best hustle for you..."):
        time.sleep(2)
        idea = fetch_side_hustle()
    st.success(f"🔥 **{idea}**")

st.markdown("---")  # Separator

# 💡 Section: Money-Making Motivation
st.markdown("### 💡 Money-Making Motivation")
st.write("Get inspired by some legendary financial wisdom! 📜💰")

if st.button("💭 Get Inspired"):
    with st.spinner("📖 Finding a powerful quote..."):
        time.sleep(2)
        quote = fetch_money_quote()
    st.info(f"📜 *{quote}*")

# 🎉 Footer
st.markdown("---")
st.markdown("💼 **Developed by Hanzala Ali Rajpoot** | 🚀 *Turn your ideas into income!*")
