import requests

url = "https://www.google.com"

resp = requests.get(url, verify = False)

print(resp.status_code)