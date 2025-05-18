import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Escape the Vape Quiz", layout="centered")
st.title("🚭 Escape the Vape: Risk Quiz")

st.markdown("Take this quick quiz to learn how vaping affects your habits, health, and decisions.")

# Questions
q1 = st.radio("1. Do you vape or have you vaped before?", ("No", "Sometimes", "Often"))
q2 = st.radio("2. Do your friends vape?", ("No", "Some of them", "Most of them"))
q3 = st.radio("3. How often do you feel cravings to vape?", ("Never", "Sometimes", "Often"))
q4 = st.radio("4. Have you tried quitting vaping?", ("Never", "Once", "Multiple times"))
q5 = st.radio("5. Do you think vaping helps with stress?", ("Not at all", "Sometimes", "Often"))
q6 = st.radio("6. Do you know the health risks of vaping?", ("Yes", "Somewhat", "Not really"))
q7 = st.radio("7. Do you vape in secret from parents or teachers?", ("Never", "Sometimes", "Often"))
q8 = st.radio("8. Do you spend money on vape products?", ("Never", "Rarely", "Often"))
q9 = st.radio("9. Have you missed class or activities because of vaping?", ("No", "Once", "More than once"))
q10 = st.radio("10. Do you want to quit vaping?", ("Yes", "Not sure", "No"))

# Risk scoring
answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
score = 0

for ans in answers:
    if ans in ["No", "Not at all", "Never", "Yes"]:
        score += 0
    elif ans in ["Some of them", "Sometimes", "Somewhat", "Once", "Rarely", "Not sure"]:
        score += 1
    else:
        score += 2

# Score display
st.subheader("📊 Your Results")
st.write(f"**Your Vape Risk Score is: {score} out of 20**")

# Feedback
if score <= 5:
    st.success("🟢 Low Risk: You’re making healthy choices — keep staying strong!")
elif score <= 12:
    st.warning("🟠 Moderate Risk: You're in a risky spot — think about your influences and habits.")
else:
    st.error("🔴 High Risk: You’re showing signs of vaping dependence. Talk to a trusted adult or seek help.")

# Pie chart visual
labels = 'Low-Risk Answers', 'High-Risk Answers'
sizes = [20 - score, score]
colors = ['#8BC34A', '#FF5722']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

# Vaping resources (only show if score > 5)
if score > 5:
    st.markdown("---")
    st.subheader("🛠 Build Your Quit Plan")

    st.markdown("Answer a few quick questions to start creating a quit strategy.")

    reason = st.text_input("👉 What's your biggest reason for wanting to quit?")
    support = st.selectbox("👥 Who can support you?", ["Parent", "Friend", "Counselor", "Teacher", "None"])
    trigger = st.text_input("⚠️ What usually makes you want to vape?")
    strategy = st.selectbox("🧠 What’s one thing you’ll do instead of vaping?", [
        "Go for a walk", "Drink water", "Call a friend", "Do a hobby", "Other"
    ])

    if st.button("Generate My Plan"):
        st.markdown("### 📄 Your Quit Plan")
        st.write(f"**Reason to quit:** {reason if reason else 'Stay healthy and in control'}")
        st.write(f"**Support system:** {support}")
        st.write(f"**Trigger to avoid:** {trigger if trigger else 'Being around others who vape'}")
        st.write(f"**Coping strategy:** {strategy}")
        st.success("👍 Take a screenshot or write this down — you've got this!")
