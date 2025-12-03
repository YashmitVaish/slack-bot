import os
import re
from slack_bolt import App
from slack_bolt.adapter.django import SlackRequestHandler
from dotenv import load_dotenv
load_dotenv(".env")

app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET'),
)


@app.event('app_mention')
def handle_app_mention(event, say, logger):
    user = event.get('user')
    text = event.get('text')
    logger.info('app_mention: %s', text)
    say(f"Hi <@{user}>! I'm active. Try messaging me directly or use `/echo`.")

@app.message(re.compile(r'^(hi|hello|hey)\\b', flags=re.IGNORECASE))
def greet_message(message, say):
    user = message.get('user')
    say(f"Hello <@{user}>! use `/echo` or mention me.")

@app.command('/echo')
def echo_command(ack, command, respond):
    ack()
    text = command.get('text') or ''
    respond(f"You said: {text}")

@app.event('app_home_opened')
def update_home_tab(event, client, logger):
    user_id = event.get('user')
    try:
        client.views_publish(
            user_id=user_id,
            view={
                "type": "home",
                "blocks": [
                    {"type": "section", "text": {"type": "mrkdwn", "text": "*Welcome to the Bot Home!*"}},
                    {"type": "section", "text": {"type": "mrkdwn", "text": "Use `/echo` to make the bot repeat you, or press the button below."}},
                    {"type": "actions", "elements": [
                        {"type": "button", "text": {"type": "plain_text", "text": "Say Hello"}, "action_id": "home_say_hello"}
                    ]}
                ]
            }
        )
    except Exception as e:
        logger.exception("Failed to publish app home: %s", e)

@app.action('home_say_hello')
def handle_home_button(ack, body, client):
    ack()
    user_id = body.get('user', {}).get('id')
    client.chat_postMessage(channel=user_id, text=f"Hello <@{user_id}> clicked home.")

handler = SlackRequestHandler(app)
