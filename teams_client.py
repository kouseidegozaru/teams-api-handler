from client import APIClient

class TeamsClient(APIClient):
    def __init__(self, token: str):
        headers = {"Authorization": f"Bearer {token}"}
        super().__init__(base_url="https://api.teams.microsoft.com/v1.0", headers=headers)

class TeamsChannelMessagesClient(TeamsClient):
    def __init__(self, token: str, team_id: str, channel_id: str):
        super().__init__(token=token)
        self.team_id = team_id
        self.channel_id = channel_id

    def get_messages(self):
        endpoint = f"teams/{self.team_id}/channels/{self.channel_id}/messages"
        return self.get(endpoint)

    def post_message(self, content: str):
        endpoint = f"teams/{self.team_id}/channels/{self.channel_id}/messages"
        data = {"content": content}
        return self.post(endpoint, data=data)
