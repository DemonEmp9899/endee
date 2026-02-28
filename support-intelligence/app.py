import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Support Intelligence", layout="wide")

st.title("🤖 Customer Support Intelligence System")

menu = st.sidebar.radio(
    "Navigation",
    ["Add Ticket", "Search Ticket", "Auto Resolve", "Dashboard"]
)

# ---------------------------
# ADD TICKET
# ---------------------------
if menu == "Add Ticket":

    st.header("➕ Add New Support Ticket")

    ticket_id = st.text_input("Ticket ID")
    issue = st.text_area("Issue Description")
    resolution = st.text_area("Resolution")

    if st.button("Submit Ticket"):

        response = requests.post(
            f"{API_URL}/add_ticket/",
            json={
                "ticket_id": ticket_id,
                "text": issue,
                "resolution": resolution
            }
        )

        if response.status_code == 200:
            st.success("Ticket added successfully!")
        else:
            st.error(response.text)


# ---------------------------
# SEARCH TICKET
# ---------------------------
elif menu == "Search Ticket":

    st.header("🔍 Semantic Ticket Search")

    query = st.text_area("Enter search query")

    if st.button("Search"):

        response = requests.post(
            f"{API_URL}/search_ticket/",
            json={"text": query}
        )

        if response.status_code == 200:
            data = response.json()
            st.subheader("Matches")

            for match in data["matches"]:
                st.write(f"🎫 Ticket ID: {match['ticket_id']}")
                st.write(f"📈 Similarity: {round(match['similarity_score'], 4)}")
                st.divider()
        else:
            st.error(response.text)


# ---------------------------
# AUTO RESOLVE
# ---------------------------
elif menu == "Auto Resolve":

    st.header("🤖 AI Auto Resolution")

    query = st.text_area("Describe customer issue")

    if st.button("Generate Resolution"):

        with st.spinner("Generating response..."):

            response = requests.post(
                f"{API_URL}/auto_resolve/",
                json={"text": query}
            )

            if response.status_code == 200:
                data = response.json()

                st.subheader("🔎 Similar Tickets")
                for match in data["matches"]:
                    st.write(f"Ticket ID: {match['ticket_id']} | Score: {round(match['similarity_score'],4)}")

                st.subheader("💡 AI Suggested Resolution")
                st.success(data["ai_generated_response"])
            else:
                st.error(response.text)


# ---------------------------
# DASHBOARD
# ---------------------------
elif menu == "Dashboard":

    st.header("📊 System Dashboard")

    response = requests.get(f"{API_URL}/dashboard/")

    if response.status_code == 200:
        data = response.json()

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Tickets", data["total_tickets"])
        col2.metric("Vector Dimension", data["vector_dimension"])
        col3.metric("Model Used", data["model_used"])

    else:
        st.error(response.text)