from dotenv import load_dotenv
from pytube import YouTube
from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import re
import sys
import os

load_dotenv()  # Load environment variables from the .env file

# Check if the API key is loaded
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("OpenAI API key is missing! Set it as an environment variable.")
else:
    print("API Key loaded successfully!")

def extract_video_url(search_query):
    videos_search = VideosSearch(search_query, limit=1)
    result = videos_search.result()
    
    if "result" in result and len(result["result"]) > 0:
        video_id = result["result"][0]["id"]
        return f"https://www.youtube.com/watch?v={video_id}"
    
    return None

def get_video_id(url):
    """Extracts the YouTube video ID from a given URL."""
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")



# def get_video_metadata(url):
#     try:
#         yt = YouTube(url)
#         print(f"Title: {yt.title}")  # Debugging
#         print(f"Channel: {yt.author}")  # Debugging
#         return {
#             "title": yt.title,
#             "channel": yt.author
#         }
#     except Exception as e:
#         print(f"Error fetching metadata: {e}")
#         return {"title": "Error", "channel": "Error"}
    
def get_video_metadata(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())  # Print entire HTML structure for debugging
        title = soup.find("meta", property="og:title")
        channel = soup.find("link", itemprop="name")
        print(f"Extracted Title: {title['content'] if title else 'None'}")
        print(f"Extracted Channel: {channel['content'] if channel else 'None'}")
        return {
            "title": title["content"] if title else "Untitled",
            "channel": channel["content"] if channel else "Unknown Channel"
        }
    except Exception as e:
        return {"title": "Error", "channel": "Error"}



# def get_video_metadata(url):
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title = soup.find("meta", property="og:title")
#         channel = soup.find("link", itemprop="name")
#         return {
#             "title": title["content"] if title else "Untitled",
#             "channel": channel["content"] if channel else "Unknown Channel"
#         }
#     except Exception as e:
#         return {"title": "Error", "channel": "Error"}


def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([line["text"] for line in transcript])
    except Exception as e:
        return f"Transcript not available: {str(e)}"
    

def get_thumbnail(video_url):
    video_id = video_url.split("v=")[-1]  # Extract video ID
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"  # High-res thumbnail

    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        return thumbnail_url
    else:
        return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"  # Fallback thumbnail


def scrape_youtube_data(url):
    video_id = get_video_id(url)
    metadata = get_video_metadata(url)
    transcript = get_video_transcript(video_id)
    thumbnail = get_thumbnail(url)
    return {
        "video_id": video_id,
        "metadata": metadata,
        "transcript": transcript,
        "thumbnail": thumbnail
    }

if __name__ == "__main__":
    search_query = input("Enter the search query for YouTube Video: ")
    youtube_url = extract_video_url(search_query)
    if youtube_url.startswith("https://"):
        data = scrape_youtube_data(youtube_url)
        print(data)
    else:
        print(youtube_url)


    
