# Post request len trang cachet.com phai authentication

import requests
from requests.auth import HTTPBasicAuth

headers = {}
d = {}
headers['Content-Type'] = 'application/json;'
headers['X-Cachet-Token'] = "9yMHsdioQosnyVK4iCVR"

# components post
#url = "https://demo.cachethq.io/api/v1/components"
#d = '{"name":"API","description":"An example description","status":1}'
#response = requests.post(url, data = d, headers = headers)
#print (response.text)

# Test incident, up len https://demo.cachethq.io/
url2 = "https://demo.cachethq.io/api/v1/incidents" 
payload = "{\"message\":\"test by bo\",\"name\":\"test incident\",\"status\":1,\"visible\":1}"
response2 = requests.request("POST", url2, data=payload, headers = headers)
print(response2)

