import requests
import os

class MessageClient:
    def __init__(self):
        self.api_key = os.environ.get('IMESSAGE_PASSWORD_KEY')
        self.base_url = os.environ.get('IMESSAGE_BASE_URL')
        self.headers = {
            "api_key": self.api_key 
        }

    def send_message(self, recipient, message, is_name=True):
        url = f"{self.base_url}/send"
        payload = {
            "recipient": recipient,
            "message": message
        }
        response = requests.post(url, json=payload, headers=self.headers, params={"name": is_name})
        return response.json()

    def get_messages(self, num_messages=10, sent=True, formatted=True):
        url = f"{self.base_url}/messages"
        response = requests.get(url, headers=self.headers, params={"num_messages": num_messages, "sent": sent, "formatted": formatted})
        return response.json()

    def get_person_messages(self, person, num_messages=10, sent=True, formatted=True, is_name=True):
        url = f"{self.base_url}/messages/{person}"
        response = requests.get(url, headers=self.headers, params={"num_messages": num_messages, "sent": sent, "formatted": formatted, "name": is_name})
        return response.json()

    def get_recent_contacts(api_key, num_contacts=10):
        url = f"{base_url}/recent_contacts"
        params = {"num_contacts": num_contacts}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()["recent_contacts"]
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

