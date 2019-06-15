import requests
from SendGrid import API_KEY

url = "https://api.sendgrid.com/v3/geo/stats?start_date=2019-06-09"

payload = "{}"
headers = {'authorization': 'Bearer {0}'.format(API_KEY)}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)