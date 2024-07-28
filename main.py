import requests
import json

url = "https://google.serper.dev/search"

q=input("Enter what you wanna search for: ")

payload = json.dumps({
  "q": q
})
headers = {
  'X-API-KEY': '126a3a211376057e5e0b93f8c10a9784ca76fa6f',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
data=response.json()

title=data['knowledgeGraph']['title']
description=data['knowledgeGraph']['description']

print(f"Title: {title}\nDescription:{description}")