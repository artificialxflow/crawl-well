# TODO: Build a self-hosted web scraper using Crawl4AI and Streamlit

## Prerequirements
- Python 3.8+
- pip (Python package manager)
- Basic knowledge of Python
- Internet connection (for installing packages and scraping)
- (Recommended) Git for version control

## Theoretical Steps
1. Familiarize with concepts and systems
   - Understand web scraping basics
   - Review Crawl4AI and its GitHub documentation
   - Understand HTML to Markdown conversion
   - Learn about Streamlit for UI
2. Plan system architecture
   - Define main code structure (dependencies, helpers, main, executable)

## Functional Steps
- [ ] Set up environment and install dependencies
  - [ ] Create Python virtual environment
  - [ ] Activate virtual environment
  - [ ] Create requirements.txt with all dependencies
  - [ ] Install dependencies (streamlit, crawl4ai, crawl4ai-sync, markdownify, beautifulsoup4, requests, base64, re)
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