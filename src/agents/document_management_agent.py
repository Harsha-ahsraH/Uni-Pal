import streamlit as st
from src.models import Document
from typing import List, Optional
import logging


def manage_documents(student_info=None) -> Optional[List[Document]]:
    """
    Manage and display document requirements for the student.

    Args:
        student_info (dict or StudentInfo, optional): Student information.

    Returns:
        A list of Document objects or None if an error occurs.
    """
    try:
        # Convert Pydantic model to dictionary if needed
        if hasattr(student_info, 'model_dump'):
           student_info = student_info.model_dump()

        # Define a list of standard documents required for university applications
        standard_documents = [
            Document(
                id=1,
                name="10th Grade Marksheet",
                status="Pending",
                required=True,
                description="Official marksheet/transcript from 10th grade"
            ),
            Document(
                id=2,
                name="12th Grade Marksheet",
                status="Pending",
                required=True,
                description="Official marksheet/transcript from 12th grade"
            ),
            Document(
                id=3,
                name="B.Tech Degree/Marksheet",
                status="Pending",
                required=True,
                description="Official B.Tech degree or latest semester marksheet"
            ),
            Document(
                id=4,
                name="IELTS/TOEFL Score",
                status="Pending",
                required=True,
                description="English proficiency test score"
            ),
            Document(
                id=5,
                name="Passport",
                status="Pending",
                required=True,
                description="Valid passport for international travel"
            ),
            Document(
                id=6,
                name="Statement of Purpose (SOP)",
                status="Pending",
                required=True,
                description="Personal essay explaining academic and career goals"
            )
        ]
        return standard_documents
    except Exception as e:
         logging.error(f"Error managing documents: {e}")
         return None


def document_checker_page():
    st.title("Document Checklist")
    student_data = st.session_state.get('student_data')
    if student_data:
        documents = manage_documents(student_data)
        if documents:
            st.success("Document checklist generated!")
            for doc in documents:
                # Use the document id as a unique key for the checkbox
                checkbox_key = f"doc_checkbox_{doc.id}"
                is_checked = st.checkbox(f"{doc.name} - {doc.description}", key=checkbox_key, value=(doc.status == "Completed"))
                if is_checked:
                    doc.status = "Completed"
                else:
                    doc.status = "Pending"
        else:
            st.error("Failed to generate document checklist.")
    else:
        st.info("Please fill in the Student Information first to generate a personalized document checklist.")

