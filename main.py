from teams_client import TeamsChannelMessagesClient
from dotenv import load_dotenv
import os

class CustomTeamsClient(TeamsChannelMessagesClient):
    def __init__(self):
        load_dotenv()
        team_id = os.getenv("TEAM_ID")
        channel_id = os.getenv("CHANNEL_ID")
        token = os.getenv("ACCESS_TOKEN")
        super().__init__(token=token, team_id=team_id, channel_id=channel_id)

def main():
    client = CustomTeamsClient()
    
    # Get messages from the channel
    messages = client.get_messages()
    print("Messages in the channel:")
    for message in messages.get("value", []):
        print(f"- {message['content']}")

    # Post a new message to the channel
    new_message_content = "Hello, this is a test message!"
    response = client.post_message(new_message_content)
    print("Posted new message:", response)

if __name__ == "__main__":
    main()