"""
Strategic Maritime Early Warning System
Executive Dashboard
"""

import streamlit as st
import pandas as pd

from intelligence.maritime_engine import generate_maritime_assessment


st.set_page_config(
    page_title="Strategic Maritime Early Warning System",
    layout="wide"
)


st.title("🌐 Strategic Maritime Early Warning System")

st.subheader(
    "Executive Maritime Risk Dashboard"
)


assessments = generate_maritime_assessment()


df = pd.DataFrame(assessments)


# KPI Section

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Vessels",
        df["vessel_count"].sum()
    )


with col2:

    st.metric(
        "Oil Tankers",
        df["oil_tankers"].sum()
    )


with col3:

    st.metric(
        "Highest Risk Score",
        df["risk_score"].max()
    )


st.divider()


# Chokepoints

st.subheader("Maritime Chokepoints Status")


for item in assessments:

    st.markdown(
        f"""
        ### 📍 {item['zone']}

        **Risk Level:** {item['risk_level']}

        **Risk Score:** {item['risk_score']}/100

        **Detected Vessels:** {item['vessel_count']}

        **Oil Tankers:** {item['oil_tankers']}

        **Strategic Impact**

        - Energy: {item['impact']['energy']}
        - Trade: {item['impact']['trade']}
        - Supply Chain: {item['impact']['supply_chain']}

        **Recommendation:**
        {item['impact']['executive_note']}

        ---
        """
    )


st.subheader("Risk Overview")

st.bar_chart(
    df.set_index("zone")["risk_score"]
)
