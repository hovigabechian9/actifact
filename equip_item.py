import json
import requests

with open("config.json", "r") as file:
    config = json.load(file)

token = config.get("token")
character = config.get("character")

url = f"https://api.artifactsmmo.com/my/{character}/action/equip"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


data = {
    "code": "wooden_staff",
    "slot": "weapon",
    "quantity": 1
}

response = requests.post(url, headers=headers, json=data)


print("Statut :", response.status_code)
print("Réponse :", response.json())
