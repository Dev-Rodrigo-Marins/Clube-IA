import requests

url = 'http://192.168.0.106/camera'
response = requests.get(url)

if response.status_code == 200:
    print(response.content)
else:
    print(f"Erro: {response.status_code}")
