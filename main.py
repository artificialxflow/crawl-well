import streamlit as st
from urllib.parse import urljoin
from markdownify import markdownify as md
import re
import base64
import requests
from bs4 import BeautifulSoup

# --- Helper Functions (to be implemented) ---
def custom_streamlit_styling():
    st.markdown(
        """
        <style>
        /* Custom Streamlit styles */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 2em;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #4CAF50;
        }
        .download-btn {
            display: inline-block;
            background: #4CAF50;
            color: white !important;
            padding: 0.5em 2em;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 1em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def resource_url_setup(page_url, img_src):
    """
    Resolve an image src (which may be relative) to an absolute URL based on the page URL.
    """
    return urljoin(page_url, img_src)

def html_to_markdown(html_content):
    """
    Convert HTML content to Markdown, preserving heading hierarchy and images.
    """
    return md(html_content, heading_style="ATX")

def markdown_cleanup(markdown_str):
    """
    Clean up the Markdown string by removing extra empty lines and unnecessary whitespace.
    """
    # Remove multiple consecutive empty lines
    cleaned = re.sub(r'\n{3,}', '\n\n', markdown_str)
    # Strip leading/trailing whitespace from each line
    cleaned = '\n'.join(line.strip() for line in cleaned.splitlines())
    # Remove leading/trailing empty lines
    cleaned = cleaned.strip()
    return cleaned

def download_button(markdown_str, filename="scraped_content.md"):
    """
    Create a styled download button for the Markdown content using Streamlit and base64 encoding.
    """
    b64 = base64.b64encode(markdown_str.encode()).decode()
    href = f'<a href="data:file/markdown;base64,{b64}" download="{filename}" class="download-btn">Download Markdown</a>'
    st.markdown(href, unsafe_allow_html=True)

# --- Main Streamlit App ---
def main():
    custom_streamlit_styling()
    st.title("Crawl4AI Web Scraper")
    st.write("This app will extract text and images from a web page and convert it to Markdown.")

    url = st.text_input("Enter the URL to scrape:")
    if st.button("Scrape and Convert"):
        if not url:
            st.error("Please enter a valid URL.")
            return
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Fix image src attributes to be absolute URLs
            for img in soup.find_all("img"):
                if img.has_attr("src"):
                    img["src"] = resource_url_setup(url, img["src"])

            html_content = str(soup)
            markdown = html_to_markdown(html_content)
            cleaned_markdown = markdown_cleanup(markdown)

            st.subheader("Markdown Output:")
            st.code(cleaned_markdown, language="markdown")
            download_button(cleaned_markdown)
        except Exception as e:
            st.error(f"Error during scraping or conversion: {e}")

if __name__ == "__main__":
    main() 