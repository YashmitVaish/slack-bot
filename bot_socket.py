import os
from dotenv import load_dotenv
load_dotenv(".env")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from slack_bolt.adapter.socket_mode import SocketModeHandler
from slackbot.app import app

if __name__ == "__main__":
    app_token = os.environ.get("SLACK_APP_TOKEN")
    handler = SocketModeHandler(app, app_token)
    handler.start()
