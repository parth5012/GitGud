"""
Standalone script to enqueue the send_issues_to_discord task.
Used by Render Cron Job as an alternative to Celery Beat.
"""
from beat import send_issues_to_discord

if __name__ == "__main__":
    result = send_issues_to_discord.delay()
    print(f"Task enqueued: {result.id}")
