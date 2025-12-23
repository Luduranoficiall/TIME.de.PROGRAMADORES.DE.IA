import logging
import re

SENSITIVE_KEYS = ["token", "password", "secret", "key"]

class MaskingFormatter(logging.Formatter):
    def format(self, record):
        msg = super().format(record)
        for key in SENSITIVE_KEYS:
            msg = re.sub(f'("{key}": ")([^"]+)(")', r'\1***\3', msg, flags=re.IGNORECASE)
        return msg

def setup_masked_logger():
    handler = logging.StreamHandler()
    formatter = MaskingFormatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logging.basicConfig(level=logging.INFO, handlers=[handler])
