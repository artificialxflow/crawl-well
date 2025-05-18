# Crawl4AI Web Scraper

A self-hosted web scraper built with Streamlit and Crawl4AI. This tool extracts text and images from web pages, converts the content to Markdown, and allows users to download the result. The app is easy to use, customizable, and runs locally in your browser.

## Features
- Extracts text and images from any public web page
- Converts HTML content to clean Markdown
- Download the scraped content as a Markdown file
- Simple, user-friendly Streamlit interface
- Custom styling for a modern look

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- (Recommended) Git for version control

## Setup Instructions
1. **Clone the repository** (if using Git):
   ```sh
   git clone <your-repo-url>
   cd <project-folder>
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv .venv
   ```
3. **Activate the virtual environment:**
   - On Windows (PowerShell):
     ```sh
     .\.venv\Scripts\Activate.ps1
     ```
   - On Windows (CMD):
     ```sh
     .\.venv\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```
4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Run the app:**
   ```sh
   streamlit run main.py
   ```

## Usage
- Enter the URL of the web page you want to scrape.
- Click "Scrape and Convert".
- View the Markdown output and download it using the provided button.

---

## Project Steps Checklist
- [ ] Set up environment and install dependencies
  - [ ] Create Python virtual environment
  - [ ] Activate virtual environment
  - [ ] Create requirements.txt with all dependencies
  - [ ] Install dependencies (streamlit, crawl4ai, markdownify, beautifulsoup4, requests)
- [ ] Implement helper functions
  - [ ] Custom Streamlit styling
  - [ ] Resource URL setup (for images)
  - [ ] HTML to Markdown conversion (with heading hierarchy)
  - [ ] Markdown cleanup (remove empty lines, whitespace)
  - [ ] Download button (base64 encoding, HTML styling)
- [ ] Build main Streamlit application
  - [ ] Input URL form
  - [ ] Scraping logic (text and images)
  - [ ] Use helper functions for processing
  - [ ] Error handling and user feedback
- [ ] Create shell executable for running app
  - [ ] Write .sh file to launch Streamlit app
  - [ ] Make shell file executable (document for Windows/Mac/Linux)
- [ ] Test the scraper and download output
  - [ ] Run app locally
  - [ ] Test scraping and Markdown download
  - [ ] Document usage and troubleshooting 