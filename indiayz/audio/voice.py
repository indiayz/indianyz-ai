from indiayz.core.base import BaseModule

class Voice(BaseModule):
    @staticmethod
    def tts(text: str):
        res = Voice._post("/api/audio", {"text": text})
        return res
