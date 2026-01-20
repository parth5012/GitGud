from discord_webhook import DiscordWebhook, DiscordEmbed

# Your Discord webhook URL
WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"

# Create the webhook object
webhook = DiscordWebhook(url=WEBHOOK_URL, content='This is a message with an embed.')

# Create an embed object
embed = DiscordEmbed(title='Example Embed Title', description='This is the description for the embed.', color='03b2f8')

# Add embed to webhook
webhook.add_embed(embed)

# Execute the webhook
response = webhook.execute()

if response.status_code in [200, 204]:
    print("Webhook executed successfully with an embed!")
else:
    print(f"Failed to execute webhook. Status code: {response.status_code}")
