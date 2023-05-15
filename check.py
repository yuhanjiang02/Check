# streamlit version
import streamlit as st
import re

def validate_file_name(file_name):
    """
    Validate the correctness of a file name.
    Returns True if the file name is valid, False otherwise.
    """
    # File name pattern: starts with a number, followed by letters, numbers, dashes, or underscores
    pattern = r'^\d.*_raw\.xlsx$'
    return re.match(pattern, file_name) is not None

def upload_and_check_file():
    """
    Upload a file and check its name correctness.
    """
    st.title("File Upload and Validation")
    st.write("Please upload a file.")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Get the file name from the uploaded file
        file_name = uploaded_file.name

        st.write(f"Uploaded file name: {file_name}")

        if validate_file_name(file_name):
            st.success("File name is correct.")
            # Perform further processing or analysis on the file here
        else:
            st.error("Invalid file name. File name should start with a number and can contain letters, numbers, dashes, or underscores.")

# Run the function
upload_and_check_file()
