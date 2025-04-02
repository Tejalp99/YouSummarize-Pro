# YouSummarize-Pro: Automated YouTube Video Summarization


![youtube-logo-hd-8-1024x768](https://github.com/user-attachments/assets/89f4b855-149a-4038-8eb1-ca9fb1757f34) 

## Project Overview
This project is an AI-powered web application that extracts metadata and transcribes YouTube videos, then generates concise summaries using OpenAI's GPT model. Built with Streamlit, it provides users with a quick and efficient way to grasp the core ideas of long-form video content without watching the entire video.

## Features
- Extracts video metadata (title and channel name)
- Retrieves video transcripts (if available)
- Generates AI-powered summaries in multiple languages
- Displays the video thumbnail
- Simple and interactive Streamlit UI

## Tech Stack
- Python 3.9+
- Streamlit (for UI)
- Pytube (for metadata extraction)
- OpenAI API (for text summarization)
- BeautifulSoup (for web scraping)
- dotenv (for API key management)

## Installation
### Prerequisites
Ensure you have Python 3.9+ installed.

### Step 1: Clone the Repository
``` bash https://github.com/Tejalp99/YouSummarize-Pro.git  ```

### Step 2: Set up a virtual environment:
``` bash python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### Step 3: Install required dependencies:
``` bash pip install -r requirements.txt```

### Step 4: Set up environment variables:
Create a .env file in the root of the project and add your OpenAI API key:

``` bash OPENAI_API_KEY=your_openai_api_key```

## Usage
1. Run the Streamlit app:
   ``` bash streamlit run app.py ```

2. In the app, you can:
   - Enter a YouTube video URL to summarize.
   - Use a search query to fetch a YouTube video and summarize it.
   - Select the language for the summary (English, Spanish, Hindi).

3. Once the video is loaded, the title, channel name, transcript, thumbnail, and summary will be displayed.

## File Structure
``` bash
YouTube-Video-Summarizer/
│
├── app.py                 # Streamlit app for the front-end
├── scrape_youtube.py      # Scraping video metadata, transcript, and thumbnail
├── summarize_text.py      # Summarizing text using OpenAI GPT
├── requirements.txt       # Required dependencies
├── .env                   # Store your OpenAI API key
├── README.md              # Project documentation
└── assets/                # Folder for additional assets (e.g., images)
```

## License
This project is licensed under the MIT License.

## Acknowledgements
- OpenAI for providing GPT models.
- YouTube API for video data extraction.
- Streamlit for building the web interface.



