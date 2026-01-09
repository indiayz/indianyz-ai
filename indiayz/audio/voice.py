from indiayz.core.base import BaseModule

class Voice(BaseModule):
    @staticmethod
    def speak(text: str):
        instance = Voice()
        result = instance._post("/api/audio", {"text": text})
        return result.get("response", "")
