import json
import requests

with open("config.json", "r") as file:
    config = json.load(file)

token = config.get("token")
character = config.get("character")

url = f"https://api.artifactsmmo.com/my/{character}/action/gathering"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)

print("Statut :", response.status_code)
print("Réponse :", response.json())
