import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import os
import json
import google.generativeai as genai
import PyPDF2 as pdf
from dotenv import load_dotenv

def configure_genai(api_key):
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        raise Exception(f"Failed to configure Generative AI: {str(e)}")
    

def get_gemini_response(prompt):
    """Generate a response using Gemini with enhanced error handling and response validation."""
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # Ensure response is not empty
        if not response or not response.text:
            raise Exception("Empty response received from Gemini")
        
        return response
    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")

def extract_pdf_text(uploaded_file):
    """Extract text from PDF with enhanced error handling."""
    try:
        reader = pdf.PdfReader(uploaded_file)
        if len(reader.pages) == 0:
            raise Exception("PDF file is empty")
            
        text = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
                
        if not text:
            raise Exception("No text could be extracted from the PDF")
            
        return " ".join(text)
        
    except Exception as e:
        raise Exception(f"Error extracting PDF text: {str(e)}")
    


def prepare_prompt(pdf_text):
    """Prepare the input prompt with improved structure and validation."""
    if not pdf_text:
        raise ValueError("pdf text cannot be empty")
        
    prompt_template = """
    Act as an expert Summarizer and make sure u do it properly.Include all the important information.
    Dont miss on crucial points.

    
    Summarize the following text extracted from a PDF and return the summary only and no extra 
    points to be added. 
    
    PDF text:
    {pdf_text}
    
    Provide response as text 
    """
    
    return prompt_template.format(
        pdf_text=pdf_text.strip()
    )

def init_session_state():
    """Initialize session state variables."""
    if 'processing' not in st.session_state:
        st.session_state.processing = False


def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize session state
    init_session_state()
    
    # Configure Generative AI
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("Please set the GOOGLE_API_KEY in your .env file")
        return
        
    try:
        configure_genai(api_key)
    except Exception as e:
        st.error(f"Failed to configure API: {str(e)}")
        return

    # Sidebar
    with st.sidebar:
        st.title("PDF Summarizer")
        st.subheader("About")
        st.write("""
        This PDF Summarizer helps you:
        - To summarize PDFs
        - In last minute prep
        """)

    # Main content
    st.title("📄 PDF Summarizer")
    st.subheader("Summarize your PDFs")
    
    # Input sections with validation
    uploaded_file = st.file_uploader(
        "Upload Document (PDF)",
        type="pdf",
        help="Upload your document in PDF format"
    )

    # Process button with loading state
    if st.button("Summarize", disabled=st.session_state.processing):
       
        if not uploaded_file:
            st.warning("Please upload a document in PDF format.")
            return
            
        st.session_state.processing = True
        
        try:
            with st.spinner("📊 Summarizing your PDF"):
                # Extract text from PDF
                pdf_text = extract_pdf_text(uploaded_file)
                
                # Prepare prompt
                input_prompt = prepare_prompt(pdf_text)
                
                # Get and parse response
                response = get_gemini_response(input_prompt)

                
                # Display results
                st.success("✨ Completed!")
                
                #summary
                st.subheader("PDF Summary")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            
        finally:
            st.session_state.processing = False

if __name__ == "__main__":
    main()