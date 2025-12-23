import os
import hvac

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

def get_secret(path: str, key: str):
    secret = client.secrets.kv.v2.read_secret_version(path=path)
    return secret['data']['data'][key]
