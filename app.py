import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🎓 CGPA Calculator & Semester Performance Analyzer")
st.write("Enter your semester SGPA and credits to calculate your overall CGPA.")

# Default number of semesters
sem_count = st.number_input("Number of semesters:", min_value=1, max_value=10, value=4, step=1)

# Create empty lists to store SGPA and credits
grades = []
credits = []

# Input for each semester
for i in range(1, sem_count + 1):
    st.subheader(f"Semester {i}")
    grade = st.number_input(f"Enter SGPA for Semester {i} (0-10):", min_value=0.0, max_value=10.0, step=0.1, key=f"g{i}")
    credit = st.number_input(f"Enter credits for Semester {i}:", min_value=1, max_value=30, step=1, key=f"c{i}")
    grades.append(grade)
    credits.append(credit)

# Calculate CGPA when button is pressed
if st.button("Calculate CGPA"):
    total_points = sum([g*c for g, c in zip(grades, credits)])
    total_credits = sum(credits)
    if total_credits == 0:
        st.warning("Total credits cannot be zero!")
    else:
        cgpa = total_points / total_credits
        st.success(f"Your CGPA is: {cgpa:.2f}")

        # Create DataFrame for visualization
        df = pd.DataFrame({
            "Semester": [f"Sem {i}" for i in range(1, sem_count + 1)],
            "SGPA": grades
        })

        # Plot semester-wise SGPA
        st.subheader("Semester-wise SGPA")
        fig, ax = plt.subplots()
        ax.bar(df["Semester"], df["SGPA"], color="skyblue")
        ax.set_ylim(0, 10)
        ax.set_ylabel("SGPA")
        ax.set_xlabel("Semester")
        ax.set_title("Semester Performance")
        st.pyplot(fig)
else:
    st.info("Fill in the semester SGPA and credits, then click 'Calculate CGPA' to see your results.")
