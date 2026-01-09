# indiayz/audio/voice.py

from indiayz.core.base import BaseModule


class Voice(BaseModule):
    """
    Audio & voice interface.
    """

    name = "audio.voice"

    @staticmethod
    def tts(text: str):
        response = Voice._post("/audio/tts", {"text": text})
        return response
