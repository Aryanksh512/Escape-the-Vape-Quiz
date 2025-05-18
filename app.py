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
    st.subheader("📘 Resources to Help You Quit")
    st.markdown("""
- [**SmokeFree Teen Quit Vaping App**](https://teen.smokefree.gov/quit-vaping): Tools, tips, and a free quit plan.
- [**Truth Initiative: This is Quitting**](https://truthinitiative.org/thisisquitting): Free text support — text "DITCHVAPE" to 88709.
- [**CDC Quit Guide**](https://www.cdc.gov/tobacco/quit_smoking/how_to_quit/index.htm): Strategies and help from professionals.
- Talk to your school counselor, a doctor, or a trusted adult about support options.
    """)
    st.info("You're not alone. Help is out there, and quitting is possible.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Escape the Vape | Educating Teens, Saving Lives.")
