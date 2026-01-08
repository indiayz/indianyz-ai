from indiayz.core.base import BaseModule


class Image(BaseModule):
    """
    Image generation & processing interface.
    """

    name = "image"

    @staticmethod
    def generate(prompt: str):
        # Placeholder
        print(f"[indiayz-image] Generating image for: {prompt}")
