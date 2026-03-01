from celery import shared_task



@shared_task(name='Send Issues to Discord')
def send_issues_to_discord():
    print("Sending issues to Discord")
    