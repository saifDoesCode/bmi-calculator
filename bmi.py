import streamlit as st
import matplotlib.pyplot as plt

def draw_bmi_chart(bmi):
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    ranges = [16, 18.5, 24.9, 29.9, 40]  

    fig, ax = plt.subplots(figsize=(15, 3))

    colors = ["#ADD8E6", "#90EE90", "#FFD580", "#FF7F7F"]

    for i in range(len(categories)):
        ax.barh(0, ranges[i+1] - ranges[i], left=ranges[i], color=colors[i], edgecolor='black')

    ax.axvline(bmi, color='black', linewidth=2)
    ax.text(bmi + 0.1, 0.15, f'Your BMI: {bmi:.1f}', fontsize=30, color='black')

    ax.set_xlim(15, 40)
    ax.set_yticks([])
    ax.set_xticks(ranges)
    ax.set_xlabel("BMI Range", fontsize = 30)
    ax.set_title("BMI Classification Chart", fontsize = 30)

    st.pyplot(fig)

st.title("🧮 BMI Calculator")

st.subheader("Enter your details: ")
height = st.number_input("Height (CM): ", min_value = 50.0, max_value = 250.0, value = 170.0)
weight = st.number_input("Weight (KG): ", min_value = 10.0, max_value = 300.0, value = 70.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f"### Your BMI is: '{bmi:.2f}' ")

    if bmi < 18.5:
        category = "Underweight"
        emoji = "🦴"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
        emoji = "✅"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        emoji = "⚠️"
    else:
        category = "Obese"
        emoji = "🚨"
    
    st.success(f"Category: **{category}** {emoji}")
    draw_bmi_chart(bmi)
