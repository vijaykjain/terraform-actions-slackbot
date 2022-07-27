import os
from dotenv import load_dotenv
from slack_bolt import App

# Initializes static variables
load_dotenv()
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SIGNING_SECRET = os.environ.get("SIGNING_SECRET")

# Initializes your app with your bot token and signing secret
app = App(
    token = SLACK_BOT_TOKEN,
    signing_secret = SIGNING_SECRET
)

# Listens to incoming messages that contain "hello" To learn available listener arguments,
@app.message("hello")
def message_hello(message, say):
    # sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 4000)))
