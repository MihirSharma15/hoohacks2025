

from pydantic import BaseModel, Field


class Transcription(BaseModel):
     """
     A simple transcription schema.
     """
     transcript: str = Field(description="The transcribed text from the audio file.")