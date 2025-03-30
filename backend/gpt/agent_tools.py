"""Framework that describes the tools available to the agent."""

from functools import lru_cache
import openai
from openai import OpenAI
from schemas.agent_schemas import Transcription
import whisper 
@lru_cache
def get_openai_client():
    """
    Returns an OpenAI client instance.
    """
    return openai.OpenAI()

def speech_to_text(audio_file_path: str, client: OpenAI) -> Transcription:
    """
    Transcribe speech from an audio file to text.
    :param audio_file_path: Path to the audio file.
    :return: Transcribed text.
    Change for later
    """
    with open(audio_file_path, "rb") as audio_file:
        model = whisper.load_model("small")
        transcription = model.transcribe(audio_file_path)

    return Transcription(transcript=transcription["text"])


def parse_command(transcribed_text: str) -> str:
    """
    Parses the transcribed text into a structured JSON command.
    The output JSON will have two keys:
      - "action": "scrape", "news", or "both"
      - "ticker": the stock ticker symbol extracted from the text
    """

    prompt = f"""
    You are a stock market command parser. Given the transcribed text, determine what type of data the user is asking for.
    Output a valid JSON object with two keys: "action" and "ticker".
    - "action" can be "scrape" for numerical stock data, "news" for news articles, or "both" for both.
    - "ticker" should be the stock ticker symbol mentioned in the text.
    For example, if the input is "Why is TSLA down?", output:
    {{"action": "both", "ticker": "TSLA"}}
    Transcribed text: {transcribed_text}
    """

client = OpenAI()