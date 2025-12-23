class Authority:
    ROOT_KEYS = {"GOD_MODE_KEY"}

    def __init__(self, key: str):
        self.key = key

    def is_authorized(self) -> bool:
        return self.key in self.ROOT_KEYS
