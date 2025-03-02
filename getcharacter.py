import requests

url = "https://api.artifactsmmo.com/my/characters"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print("Statut :", response.status_code)
print("Contenu :", response.json())
