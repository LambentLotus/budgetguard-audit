import streamlit as st

st.set_page_config(page_title="BudgetGuard Audit", layout="centered")
st.title("🛡️ BudgetGuard: The Community Transparency Audit")
st.write("An open-source financial checkpoint ensuring public and donor funds reach the ground.")

# Core Framework Intakes
org_name = st.text_input("Name of Organization, Project, or Department:", value="Local Volunteer Relief Fund")
total_budget = st.number_input("Total Overall Budget / Capital Raised ($):", min_value=1.0, value=50000.0, step=1000.0)

st.divider()
st.subheader("📊 Complete Expense Allocation Breakdown")
st.write("Input the raw expenditure numbers below to map out the entire budget footprint:")

# Simple Visual Columns for Everyday Users
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🪵 1. The Ground Work")
    direct_cause = st.number_input("Spent Directly on the Cause ($)\n(e.g., Food, supplies, medical aid, direct field items)", min_value=0.0, value=38000.0, step=500.0)
    field_ops = st.number_input("Basic Field Operations ($)\n(e.g., Delivery vehicles, gear, tools, on-site setup costs)", min_value=0.0, value=4000.0, step=100.0)

with col2:
    st.markdown("### 🏢 2. The Back-Office")
    admin_salaries = st.number_input("Executive & Staff Salaries ($)\n(e.g., Director pay, internal stipends, administrative payroll)", min_value=0.0, value=6000.0, step=500.0)
    marketing_overhead = st.number_input("Office Overhead & Promo ($)\n(e.g., Advertising, office rent, travel, flyers, consultants)", min_value=0.0, value=2000.0, step=100.0)

# The Transparency Calculation Core
total_spent = direct_cause + field_ops + admin_salaries + marketing_overhead
unspent_balance = total_budget - total_spent

# Group into layman terms: Impact vs. Bureaucracy
total_impact_spending = direct_cause + field_ops
total_back_office_spending = admin_salaries + marketing_overhead

impact_percentage = (total_impact_spending / total_budget) * 100 if total_budget > 0 else 0.0
back_office_percentage = (total_back_office_spending / total_budget) * 100 if total_budget > 0 else 0.0

st.divider()

# High-Contrast Layman Results Section
st.subheader(f"📋 Transparency Integrity Score for: {org_name}")

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    st.metric(label="🎯 COMMUNITY IMPACT RATE (Money on the Ground)", value=f"{impact_percentage:.1f}%")
with metric_col2:
    st.metric(label="💼 BACK-OFFICE CONSUMPTION RATE (Overhead / Leakage)", value=f"{back_office_percentage:.1f}%")

# Instant Public Accountability Logic
if total_spent > total_budget:
    st.error(f"⚠️ DEFICIT ALERT: Expenditures exceed the total declared budget by ${abs(unspent_balance):,.2f}.")
else:
    st.info(f"🪙 Reserve Status: ${unspent_balance:,.2f} remains unspent in the organizational vault.")
    
    if impact_percentage >= 85.0:
        st.success("🌟 ELITE INTEGRITY SCORE: Exceptional financial stewardship. Maximum funding is hitting the ground.")
    elif impact_percentage >= 70.0:
        st.success("🟢 STANDARD HEALTHY LEVEL: This budget shows standard, responsible resource distribution thresholds.")
    elif impact_percentage >= 50.0:
        st.warning("⚠️ ELEVATED ADMINISTRATIVE LEAKAGE: Over 30% of funds are locked up in internal back-office expenses. Investigate administrative cost efficiency.")
    else:
        st.error("🚨 HIGH OVERHEAD ALARM: Bureaucracy is consuming the majority of this budget. More money is going to salaries and office operations than to the actual community cause.")
