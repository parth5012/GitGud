from celery import shared_task
from utils.notifier import send_content_to_discord
from utils.graphs import build_beat_graph
from utils.states import CoreState

@shared_task(name='Send Issues to Discord')
def send_issues_to_discord():
    print("Sending issues to Discord")
    workflow = build_beat_graph()
    output : CoreState = workflow.invoke({
        'user_goal': 'To start with Open Source and long term contributions.',
        'user_stack': 'Python,django,Celery,Langchain,Langgraph,Sklearn'
    })
    send_content_to_discord(output['scored_issues'])

    