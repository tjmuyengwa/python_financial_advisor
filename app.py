# app.py

import streamlit as st
from advisor_agent import run_financial_advisor

st.set_page_config(page_title="Financial Advisor AI", layout="centered")
st.title("🤓 Josh the Financial Advisor")

# 1) User Profile Inputs
with st.form("profile_form"):
    st.header("Enter Your Financial Profile")

    income = st.number_input("Annual Income (USD)", min_value=0, value=70000, step=1000)

    st.subheader("Monthly Expenses")
    housing     = st.number_input("  • Housing",      min_value=0, value=1500, step=50)
    food        = st.number_input("  • Food",         min_value=0, value=600,  step=50)
    transport   = st.number_input("  • Transport",    min_value=0, value=300,  step=50)
    entertainment = st.number_input("  • Entertainment",min_value=0, value=200,  step=50)
    others      = st.number_input("  • Others",       min_value=0, value=150,  step=50)

    goals_text = st.text_input(
        "Financial Goals (comma‑separated)",
        value="save for a house, retire at 60",
    )

    risk = st.selectbox(
        "Risk Tolerance",
        options=["low", "moderate", "high"],
        index=1,
    )

    submitted = st.form_submit_button("Get Advice")

if submitted:
    user_data = {
        "income": income,
        "monthly_expenses": {
            "housing":     housing,
            "food":        food,
            "transport":   transport,
            "entertainment": entertainment,
            "others":      others,
        },
        "financial_goals": [g.strip() for g in goals_text.split(",") if g.strip()],
        "risk_tolerance": risk,
    }

    with st.spinner("Thinking…."):
        plan = run_financial_advisor(user_data)

    st.markdown("## Your Personalized Financial Plan")
    st.write(plan)
