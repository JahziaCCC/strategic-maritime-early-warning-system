import streamlit as st


st.set_page_config(
    page_title="Strategic Maritime Early Warning System",
    layout="wide"
)


st.title("🌐 Strategic Maritime Early Warning System")

st.subheader("Executive Maritime Intelligence Dashboard")


st.metric(
    "Global Maritime Risk Index",
    "42 / 100"
)


st.divider()


col1, col2, col3 = st.columns(3)


with col1:
    st.header("🟡 مضيق هرمز")
    st.metric("Risk Score", "58")
    st.write("Impact: Energy")


with col2:
    st.header("🟢 باب المندب")
    st.metric("Risk Score", "27")
    st.write("Impact: Trade")


with col3:
    st.header("🟢 قناة السويس")
    st.metric("Risk Score", "18")
    st.write("Impact: Supply Chain")


st.divider()

st.subheader("Executive Recommendation")

st.success(
    "استمرار المراقبة وتعزيز المتابعة للممرات البحرية الحيوية"
)
