import requests
from indiayz.core.config import BASE_URL, TIMEOUT

class BaseModule:
    @staticmethod
    def _post(endpoint, payload, timeout=TIMEOUT):
        r = requests.post(f"{BASE_URL}{endpoint}", json=payload, timeout=timeout)
        r.raise_for_status()
        return r.json()
