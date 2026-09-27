import streamlit as st
from src.pipelines.pipeline import run_research_pipeline

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Multi-Agent Research System")
st.caption("Search → Scrape → Write → Critique, powered by Claude")

topic = st.text_input(
    "Enter a research topic:",
    placeholder="Example: Latest developments in quantum computing"
)

if st.button("Run Research"):
    if topic:
        with st.status("Running research pipeline...", expanded=True) as status:
            st.write("🔎 Searching, scraping, writing and reviewing...")
            state = run_research_pipeline(topic)
            status.update(label="Research complete!", state="complete")

        st.subheader("📄 Final Report")
        st.write(state["report"])

        with st.expander("🔍 View Search Results"):
            st.write(state["search_results"])

        with st.expander("📖 View Scraped Content"):
            st.write(state["scraped_content"])

        with st.expander("✅ Critic Feedback"):
            st.write(state["feedback"])
    else:
        st.warning("Please enter a topic first.")