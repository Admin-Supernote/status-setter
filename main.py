import os
import requests

# Recupera il token del bot e il messaggio di stato dalle variabili di ambiente
TOKEN = os.getenv("DISCORD_TOKEN")
STATUS_MESSAGE = os.getenv("STATUS_MESSAGE")

# Verifica che il token e il messaggio siano stati correttamente recuperati
if not TOKEN or not STATUS_MESSAGE:
    print("Errore: Assicurati che le variabili d'ambiente DISCORD_TOKEN e STATUS_MESSAGE siano impostate.")
    exit(1)

# Definisci l'endpoint API di Discord per aggiornare lo stato del bot
url = "https://discord.com/api/v9/users/@me/settings"

# Headers necessari per l'autenticazione e il formato della richiesta
headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

# Corpo della richiesta per impostare il nuovo stato
payload = {
    "custom_status": {
        "text": STATUS_MESSAGE
    }
}

# Invia la richiesta PATCH all'API di Discord per aggiornare lo stato
response = requests.patch(url, headers=headers, json=payload)

# Verifica se la richiesta è stata completata con successo
if response.status_code == 200:
    print("Stato del bot aggiornato con successo!")
else:
    print(f"Errore nell'aggiornamento dello stato: {response.status_code}")
