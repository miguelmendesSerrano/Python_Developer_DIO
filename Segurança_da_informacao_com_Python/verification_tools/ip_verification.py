""" IP verification """

import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
region = data['region']
country = data['country']

print('=' * 50)
print(f'{"IP details":^50}')
print('=' * 50)
print(f'IP: {ip}\nOrg.: {org}\nCity: {city}\nRegion: {region}\nCountry: {country}')
print('=' * 50)
