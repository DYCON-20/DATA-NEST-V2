import requests
from setting import WEBHOOK  # Assurez-vous que WEBHOOK est défini dans setting.py

def send_message_with_button(webhook_url):
    # Vérifier si l'URL du webhook est valide
    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        print("L'URL du webhook Discord est invalide.")
        return False

    # Créer le payload JSON avec le message et le bouton
    payload = {
        "content": "Cliquez sur le bouton ci-dessous pour confirmer",
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "Confirmer",
                        "style": 1,
                        "url": "https://example.com"
                    }
                ]
            }
        ]
    }

    # Envoyer le message au webhook Discord
    response = requests.post(webhook_url, json=payload)

    return response.ok

def main():
    # URL du webhook Discord
    webhook_url = f"https://discord.com/api/webhooks/{WEBHOOK}"

    # Envoyer le message avec le bouton
    if send_message_with_button(webhook_url):
        print("Message envoyé avec succès")
    else:
        print("Erreur lors de l'envoi du message")

if __name__ == "__main__":
    main()
