# Exemplo de Integração com Gemini (Python)

```python
import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=SUA_API_KEY"
headers = {"Content-Type": "application/json"}
data = {
    "contents": [{"parts": [{"text": "Olá, Gemini!"}]}]
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
```

---

# Exemplo de Integração com WhatsApp (Twilio, Python)

```python
from twilio.rest import Client

account_sid = 'SEU_SID'
auth_token = 'SEU_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Mensagem automática via WhatsApp!',
    to='whatsapp:+55SEUNUMERO'
)
print(message.sid)
```

---

# Exemplo de Automação com Google Calendar (Python)

```python
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credenciais.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

event = {
  'summary': 'Reunião de Teste',
  'start': {'dateTime': '2025-12-23T10:00:00-03:00', 'timeZone': 'America/Sao_Paulo'},
  'end': {'dateTime': '2025-12-23T11:00:00-03:00', 'timeZone': 'America/Sao_Paulo'},
}
service.events().insert(calendarId='primary', body=event).execute()
```

---

# Exemplo de Exportação para Excel (Python)

```python
import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno'],
    'Idade': [28, 34]
})
df.to_excel('dados.xlsx', index=False)
```
