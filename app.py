import streamlit as st
import os
from scrape_youtube import get_video_metadata, get_video_transcript, get_thumbnail, get_video_id
from summarize_text import summarize_text

def display_header():
    title_text = "Youtube AI Video Summarizer"
    image_url = "https://i.pinimg.com/originals/3a/36/20/3a36206f35352b4230d5fc9f17fcea92.png"

    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(image_url, width=60) 
    with col2:
        st.markdown(f"## 🎥 {title_text}")
    
    st.markdown("<p style = 'font-size:16px; color: black;'>Summarize YouTube videos using AI</p>", unsafe_allow_html=True)
    st.title(title_text)

def get_thumbnail_from_url(url):
    return get_thumbnail(url)

def get_transcript_from_url(url):
    video_id = get_video_id(url)
    return get_video_transcript(video_id)

def summarize_transcript(transcript, lang):
    summary = summarize_text(transcript, lang=lang)
    return summary

def main():
    display_header()
    st.subheader("Enter the YouTube URL:")
    st.write("Paste a Youtube link to summarize its content (must have a transcript available)")
    url = st.text_input("URL")

    language = st.radio("Select the language for the summary:", ("English", "Spanish", "Hindi"))

    if st.button("Summarize"):
        if url:
            metadata = get_video_metadata(url)
            title, channel = metadata["title"], metadata["channel"]
            
            st.subheader(f"Title:")
            st.write(title)
            st.subheader(f"Channel:")
            st.write(channel)

            thumbnail_path = get_thumbnail_from_url(url)
            if thumbnail_path != " Thumbnail not available":
                st.image(thumbnail_path, caption="Thumbnail", use_column_width=True)
            else:
                st.warning("Thumbnail not available")

            # Display the summary
            transcript = get_transcript_from_url(url)
            summary = summarize_transcript(transcript, language)
            st.subheader("Video Summary:")
            st.write(summary)
        else:
            st.warning("Please enter a valid YouTube URL")
    # if st.button("Summarize"):
    #     if url:
    #         title, channel = get_video_metadata(url)
    #         st.subheader(f"Title:")
    #         st.write(title)
    #         st.subheader(f"Channel:")
    #         st.write(channel)

    #         thumbnail_path = get_thumbnail_from_url(url)
    #         if thumbnail_path != " Thumbnail not available":
    #             st.image(thumbnail_path, caption="Thumbnail", use_column_width=True)
    #         else:
    #             st.warning("Thumbnail not available")

    #         #Display the summary
    #         transcript = get_transcript_from_url(url)
    #         summary = summarize_transcript(transcript, language)
    #         st.subheader("Video Summary:")
    #         st.write(summary)
    #     else:
    #         st.warning("Please enter a valid YouTube URL")

if __name__ == "__main__":
    main()





