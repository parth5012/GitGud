import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook


load_dotenv()

URL=os.getenv('DISCORD_WEBHOOK')

def send_content_to_discord(content:str) -> None:
    webhook = DiscordWebhook(url=URL,content=content)
    response = webhook.execute()
    if response.status_code in [200, 204]:
        print("Webhook executed successfully with an embed!")
    else:
        print(f"Failed to execute webhook. Status code: {response.status_code}")
        