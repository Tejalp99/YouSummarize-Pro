import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Check if the OpenAI API key is set
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key is missing! Set it as an environment variable.")

# Use the OpenAI API key in your script
openai.api_key = openai_api_key

def summarize_text(text, lang='en'):
    """Summarizes the given text using OpenAI's GPT model and returns structured output."""
    
    # Retrieve API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Check if API key is set
    if not openai.api_key:
        raise ValueError("OpenAI API key is missing! Set it as an environment variable.")

    # Define the prompt with structured output
    prompt = f"""
            The following text is in its original language. Provide the output in this language: {lang}. 
            Format the output as follows:
            Summary:
            A short summary of the video.

            Key Takeaways:
            - Succinct bullet point list of key takeaways.

            Input text: {text}
            """

    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4-turbo" for better performance
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the response text
        summary_text = response.choices[0].message["content"]
        return summary_text.strip()

    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

if __name__ == "__main__":
    # Get user input
    text_to_summarize = input("Enter the text to summarize: ")
    lang = input("Enter the language for the summary (default: English): ") or "en"

    # Generate and display the summary
    summary = summarize_text(text_to_summarize, lang)
    if summary:
        print("\nSummary:\n")
        print(summary)
    else:
        print("Failed to generate a summary.")