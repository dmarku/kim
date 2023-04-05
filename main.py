import requests

response = requests.get('https://httpbin.org/ip')
ip = response.json()['origin']
print(f'Your IP is {ip}')
