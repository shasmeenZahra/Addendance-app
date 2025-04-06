import streamlit as st
import pandas as pd
from PIL import Image
import io
from datetime import date

# Initialize session state for storing students
if 'students' not in st.session_state:
    st.session_state.students = []

# Sidebar Navigation
st.sidebar.title("📚 Attendance App")
page = st.sidebar.radio("Navigate", ["🧍 Add Student", "🏫 All Classes", "✅ Active Students"])

# Dummy data for All Classes
classes_data = {
    "title": "English",
    "start_date": "03-Jan-2023",
    "end_date": "31-Jul-2023",
    "days": ["Monday", "Wednesday", "Saturday"],
    "incharge": {
        "name": "Sir Zia",
        "address": "karachi",
        "contact": "+13713698110",
        "email": "xyzgmail.com"
    }
}

# Add Student Page
if page == "🧍 Add Student":
    st.title(" Add Student")
    with st.form("add_student_form"):
        st.subheader("👤 Student Details")
        name = st.text_input("Name")
        dob = st.date_input("Date of Birth", value=date(2008, 3, 11))
        age = st.number_input("Age", min_value=1, max_value=100, value=15)
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        email = st.text_input("Email")
        st.markdown("**Take Photo using Camera**")
        photo = st.camera_input("Take a photo")

        st.subheader("🙎🏻‍♂️father Details")
        father_name = st.text_input("Father Name")
        father_email = st.text_input("Father Email")

        submit = st.form_submit_button("Add Student")

        if submit:
            student_data = {
                "name": name,
                "dob": dob,
                "age": age,
                "gender": gender,
                "email": email,
                "photo": photo.getvalue() if photo else None,
                "father_name": father_name,
                "father_email": father_email,
                "status": "Active",
                "id": len(st.session_state.students) + 1
            }
            st.session_state.students.append(student_data)
            st.success("✅ Student added successfully!")

# All Classes Page
elif page == "🏫 All Classes":
    st.title("📘 All Classes")
    st.subheader(f"Class Title: {classes_data['title']}")
    st.write(f"**Starting Date:** {classes_data['start_date']}")
    st.write(f"**Ending Date:** {classes_data['end_date']}")
    st.write(f"**Days Meet:** {', '.join(classes_data['days'])}")

    st.subheader("👨‍🏫 Class In-charge")
    st.write(f"**Name:** {classes_data['incharge']['name']}")
    st.write(f"**Address:** {classes_data['incharge']['address']}")
    st.write(f"**Contact:** {classes_data['incharge']['contact']}")
    st.write(f"**Email:** {classes_data['incharge']['email']}")

    st.subheader("👥 Students")
    for student in st.session_state.students:
        st.markdown(f"**ID:** {student['id']} | **Name:** {student['name']} | **Age:** {student['age']}")

# Active Students Page
elif page == "✅ Active Students":
    st.title("🟢 Active Students")
    for student in st.session_state.students:
        if student['status'] == "Active":
            st.subheader(f"{student['name']}")
            cols = st.columns([1, 3])
            if student['photo']:
                image = Image.open(io.BytesIO(student['photo']))
                cols[0].image(image, width=100)
            cols[1].markdown(f"""
                **Registration Number:** {student['id']}  
                **Date of Birth:** {student['dob']}  
                **Age:** {student['age']}  
                **Gender:** {student['gender']}  
                **Email:** {student['email']}  
                **Student Status:** {student['status']}  
                **Father Name:** {student['father_name']}  
                **Father Email:** {student['father_email']}  
            """)
            st.markdown("---")
