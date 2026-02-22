import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import zipfile
import tempfile
import os

from ai_reviewer.core.scan_engine import run_scan
from ai_reviewer.reports.html_report import generate_html_report


st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Reviewer Dashboard")
st.markdown("---")

# 🔹 Upload ZIP or use path
uploaded_file = st.file_uploader("📦 Upload a ZIP project", type=["zip"])

scan_path = None

if uploaded_file:
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "project.zip")

    with open(zip_path, "wb") as f:
        f.write(uploaded_file.read())

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    scan_path = temp_dir
else:
    scan_path = st.text_input("📁 Or enter directory path:", ".")


if st.button("🚀 Run Analysis") and scan_path:
    with st.spinner("Scanning project..."):
        results, overall = run_scan(scan_path)

    # 🔹 Summary
    total_files = len(results)
    total_issues = sum(len(r["issues"]) for r in results)

    col1, col2, col3 = st.columns(3)
    col1.metric("📂 Files Scanned", total_files)
    col2.metric("📊 Overall Coverage", f"{overall}%")
    col3.metric("🚨 Total Issues", total_issues)

    st.markdown("---")

    # 🔹 Charts Data
    severity_counter = Counter()
    coverage_data = []

    for result in results:
        coverage_data.append({
            "File": result["file"],
            "Coverage": result["coverage"]
        })

        for issue in result["issues"]:
            severity_counter[issue["severity"]] += 1

    col_chart1, col_chart2 = st.columns(2)

    # Coverage Chart
    with col_chart1:
        st.subheader("📊 File-wise Coverage")
        df_coverage = pd.DataFrame(coverage_data)
        if not df_coverage.empty:
            st.bar_chart(df_coverage.set_index("File"))

    # Severity Chart
    with col_chart2:
        st.subheader("🚨 Severity Distribution")
        if severity_counter:
            fig, ax = plt.subplots()
            ax.pie(
                severity_counter.values(),
                labels=severity_counter.keys(),
                autopct="%1.1f%%"
            )
            st.pyplot(fig)
        else:
            st.success("No issues found 🎉")

    st.markdown("---")

    # 🔹 Detailed Results
    st.subheader("📋 Detailed Analysis")

    for result in results:
        with st.expander(f"📁 {result['file']}"):
            st.write(f"**Functions:** {result['functions']}")
            st.write(f"**Coverage:** {result['coverage']}%")

            st.markdown("### Issues")
            if result["issues"]:
                for issue in result["issues"]:
                    st.write(issue)
            else:
                st.success("No issues found.")

            st.markdown("### Style Issues")
            if result["style_issues"]:
                for style_issue in result["style_issues"]:
                    st.code(style_issue)
            else:
                st.success("No style issues.")

    # 🔹 Download HTML Report
    html_content = generate_html_report(results, overall)

    st.markdown("---")
    st.subheader("📄 Download Report")

    st.download_button(
        label="⬇️ Download HTML Report",
        data=html_content,
        file_name="ai_code_review_report.html",
        mime="text/html"
    )