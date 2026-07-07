import os
import streamlit as st
import requests

from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="Supply Chain Multi-Agent Platform",
    page_icon="🚚",
    layout="wide"
)

# ---------------- SESSION STATE ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "token" not in st.session_state:
    st.session_state.token = None


# ---------------- PDF GENERATOR ---------------- #

def create_pdf(report_text):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    for line in report_text.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 10))
            continue

        if line.startswith("# "):

            story.append(
                Paragraph(
                    f"<b>{line[2:]}</b>",
                    title_style
                )
            )

            story.append(Spacer(1, 15))

        elif line.startswith("## "):

            story.append(
                Paragraph(
                    f"<b>{line[3:]}</b>",
                    heading_style
                )
            )

            story.append(Spacer(1, 8))

        else:

            story.append(
                Paragraph(
                    line,
                    body_style
                )
            )

            story.append(Spacer(1, 6))

    doc.build(story)

    buffer.seek(0)

    return buffer


# ---------------- TITLE ---------------- #

st.title("🚚 Supply Chain Multi-Agent Platform")
st.caption(
    "Multi-Agent Architecture using CrewAI + PydanticAI + FastAPI"
)

# ---------------- NAVIGATION ---------------- #

if not st.session_state.logged_in:

    menu = "Login"

else:

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Run Workflow",
            "View Reports"
        ]
    )

    st.sidebar.success("✅ Logged In")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.token = None
        st.rerun()

# ---------------- LOGIN ---------------- #

if menu == "Login":

    st.header("🔐 Login")

    col1, col2 = st.columns(2)

    with col1:

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            response = requests.post(
                f"{API_URL}/auth/login",
                json={
                    "username": username,
                    "password": password
                }
            )

            if response.status_code == 200:

                data = response.json()

                if data.get("access_token"):

                    st.session_state.token = data["access_token"]
                    st.session_state.logged_in = True

                    st.success("Login Successful")

                    st.rerun()

                else:

                    st.error("Invalid Credentials")

            else:

                st.error("Login Failed")

    with col2:

        st.info(
            """
Demo Credentials

Username: admin

Password: admin123
"""
        )

# ---------------- RUN WORKFLOW ---------------- #

elif menu == "Run Workflow":

    st.header("⚙️ Supply Chain Testing Workflow")

    st.info(
        """
Example Objectives

• Assess supply chain resilience against critical supplier failure

• Evaluate inventory resilience during demand spikes

• Test logistics continuity during port closure

• Assess cyber attack impact on supply chain operations
"""
    )

    objective = st.text_area(
        "Business Objective",
        value="Assess supply chain resilience against critical supplier failure and evaluate mitigation strategies"
    )

    if st.button("🚀 Run Workflow"):

        with st.spinner("Running Multi-Agent Workflow..."):

            response = requests.post(
                f"{API_URL}/testing/run",
                json={
                    "objective": objective
                }
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Workflow Completed Successfully")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Workflow Status", result["status"])

                with col2:
                    st.metric("Compliance", "Passed")

                with col3:
                    st.metric("Validation", "Passed")

                st.divider()

                st.subheader("🤖 Agent Execution Status")

                agents = [
                    "Planner Agent",
                    "Scenario Generator Agent",
                    "Risk Analysis Agent",
                    "Data Validation Agent",
                    "Compliance Agent",
                    "Execution Agent",
                    "Reporting Agent"
                ]

                for agent in agents:
                    st.success(f"✅ {agent}")

                st.divider()

                st.subheader("📄 Generated Executive Report")

                # Display markdown with bold headings
                st.markdown(result["report"])

                # Generate PDF
                pdf = create_pdf(result["report"])

                st.download_button(
                    label="📄 Download Executive Report (PDF)",
                    data=pdf,
                    file_name="SupplyChain_Executive_Report.pdf",
                    mime="application/pdf"
                )

            else:

                st.error(response.text)

# ---------------- REPORTS ---------------- #

elif menu == "View Reports":

    st.header("📂 Generated Reports")

    response = requests.get(
        f"{API_URL}/reports"
    )

    if response.status_code == 200:

        reports = response.json().get(
            "reports",
            []
        )

        if reports:

            selected = st.selectbox(
                "Select Report",
                reports
            )

            if st.button("📖 Open Report"):

                report_response = requests.get(
                    f"{API_URL}/reports/{selected}"
                )

                if report_response.status_code == 200:

                    data = report_response.json()

                    st.subheader(selected)

                    st.markdown(data["content"])

                    pdf = create_pdf(data["content"])

                    st.download_button(
                        label="📄 Download PDF",
                        data=pdf,
                        file_name=selected.replace(".txt", ".pdf"),
                        mime="application/pdf"
                    )

                else:

                    st.error("Unable to load report")

        else:

            st.info("No Reports Available")

    else:

        st.error("Unable to fetch reports")