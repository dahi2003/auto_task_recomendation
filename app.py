import pickle

import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_role_data():
    with open("role.pkl", "rb") as f:
        return pickle.load(f)


# data=pickle.load(open("role_dict.pkl",'rb'))  # Update path to your actual CSV file
data=load_role_data()


st.title("📋 Unified Viewer: Role Tasks & Task Subtasks")

# -- Role Viewer Section --
st.header("🧑‍💼 View Tasks by Role")
role_input = st.text_input("Enter role keyword:")

if role_input:
    role_matches = data[data['Role'].str.contains(role_input, case=False, na=False)]

    if role_matches.empty:
        st.warning("No matching roles found.")
    else:
        for _, row in role_matches.iterrows():
            tasks = [f"• {t.strip()}" for t in row['Tasks'].split('|')]
            task_block = "<br>".join(tasks)
            st.markdown(f"### 🧾 Role: `{row['Role']}`")
            st.markdown(task_block, unsafe_allow_html=True)
            st.markdown("---")

# -- Task Viewer Section --
st.header("🧠 View Subtasks by Task")
task_input = st.text_input("Enter task keyword:")

if task_input:
    task_matches = data[data['Task_input'].str.contains(task_input, case=False, na=False)]

    if task_matches.empty:
        st.warning("No matching tasks found.")
    else:
        for _, row in task_matches.iterrows():
            subtasks = [f"• {s.strip()}" for s in row['Predicted_Subtasks'].split('|')]
            subtask_block = "<br>".join(subtasks)
            st.markdown(f"### 🧩 Task: `{row['Task_input']}`")
            st.markdown(subtask_block, unsafe_allow_html=True)
            st.markdown("---")
