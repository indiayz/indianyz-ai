from indiayz.core.base import BaseModule

class Video(BaseModule):
    @staticmethod
    def download(url: str):
        res = Video._post("/api/video", {"url": url})
        return res
