import streamlit as st
import matplotlib.pyplot as plt
import openai  # for AI responses

# 🔑 Set your OpenAI API key (secure this if deploying publicly!)
openai.api_key = "your-api-key"  # Replace with your actual key or use os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Escape the Vape Quiz", layout="centered")
st.title("🚭 Escape the Vape: Risk Quiz")

st.markdown("Take this quick quiz to learn how vaping affects your habits, health, and decisions.")

# Quiz Questions
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

# Scoring
answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
score = 0

for ans in answers:
    if ans in ["No", "Not at all", "Never", "Yes"]:
        score += 0
    elif ans in ["Some of them", "Sometimes", "Somewhat", "Once", "Rarely", "Not sure"]:
        score += 1
    else:
        score += 2

# Results
st.subheader("📊 Your Results")
st.write(f"**Your Vape Risk Score is: {score} out of 20**")

# Risk Feedback
if score <= 5:
    st.success("🟢 Low Risk: You’re making healthy choices — keep staying strong!")
elif score <= 12:
    st.warning("🟠 Moderate Risk: You're in a risky spot — think about your influences and habits.")
else:
    st.error("🔴 High Risk: You’re showing signs of vaping dependence. Talk to a trusted adult or seek help.")

# Pie Chart
labels = ['Low-Risk Answers', 'High-Risk Answers']
sizes = [20 - score, score]
colors = ['#8BC34A', '#FF5722']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

# Quit Plan + AI Generator
if score > 5:
    st.markdown("---")
    st.subheader("🛠 Build Your Quit Plan")

    st.markdown("Answer a few questions to start creating a personalized strategy.")

    reason = st.text_input("👉 What's your biggest reason for wanting to quit?")
    support = st.selectbox("👥 Who can support you?", ["Parent", "Friend", "Counselor", "Teacher", "None"])
    trigger = st.text_input("⚠️ What usually makes you want to vape?")
    strategy = st.selectbox("🧠 What’s one thing you’ll do instead of vaping?", [
        "Go for a walk", "Drink water", "Call a friend", "Do a hobby", "Other"
    ])

    if st.button("Generate My Plan"):
        # Build AI prompt
        prompt = f"""Create a personalized and encouraging quit vaping plan for a teenager.
Reason for quitting: {reason}
Support system: {support}
Trigger: {trigger}
Coping strategy: {strategy}

Use positive, realistic language that's supportive and teen-friendly."""

        with st.spinner("Generating your plan..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8,
                    max_tokens=300
                )
                plan_text = response['choices'][0]['message']['content']
                st.markdown("### 📄 Your AI-Powered Quit Plan")
                st.write(plan_text)
                st.success("👍 You've taken the first step. Keep going!")
            except Exception as e:
                st.error("⚠️ Something went wrong generating your plan. Please try again.")
                st.text(str(e))

