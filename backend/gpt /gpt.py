"""
All functionality related to using gpt
"""

import whisper

def transcribe_audio(path: str) -> str:
    """
    Convert audio to text
    """
    model = whisper.load_model("small")
    result = model.transcribe(path)
    print(result["text"])

if __name__ == "__main__":
    transcribe_audio("test.mp3")
