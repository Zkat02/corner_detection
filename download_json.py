import requests

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"

response = requests.get(url)
with open("deviation.json", "wb") as file:
    file.write(response.content)
