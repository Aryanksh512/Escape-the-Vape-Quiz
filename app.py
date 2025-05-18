import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Escape The Vape: Vape Risk Quiz & Dashboard")

# Step 1: Quiz questions
st.header("Vape Risk Quiz")

q1 = st.radio("Do you vape or have you vaped before?", ("No", "Sometimes", "Often"))
q2 = st.radio("Do your friends vape?", ("No", "Some of them", "Most of them"))
q3 = st.radio("How often do you feel cravings to vape?", ("Never", "Sometimes", "Often"))

# Calculate risk score
score = 0
score += 0 if q1 == "No" else (1 if q1 == "Sometimes" else 2)
score += 0 if q2 == "No" else (1 if q2 == "Some of them" else 2)
score += 0 if q3 == "Never" else (1 if q3 == "Sometimes" else 2)

st.write(f"Your Vape Risk Score is: **{score}** out of 6")

if score <= 2:
    st.success("Low risk — keep it up!")
elif score <= 4:
    st.warning("Moderate risk — be careful!")
else:
    st.error("High risk — consider seeking help!")

# Step 2: Display vaping trend chart (example data)
st.header("Vaping Trends in Teens")

data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Percent Vaping": [20, 25, 28, 22, 18]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.plot(df["Year"], df["Percent Vaping"], marker='o')
ax.set_ylabel("Percent Vaping (%)")
ax.set_xlabel("Year")
ax.set_title("Teen Vaping Trend Over Years")
st.pyplot(fig)

# Step 3: Tips to quit vaping
st.header("Tips to Quit Vaping")
st.write("""
- Set clear goals and track your progress  
- Avoid triggers and vape-free zones  
- Seek support from friends, family, or counselors  
- Use apps or resources designed to help quit  
""")
