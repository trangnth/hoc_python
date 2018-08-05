# Them header va cookie vao yeu cau gui den may chu, su dung dictionary truyen vao tham so cookie

import requests

url = 'http://some-domain.com/set/cookies/headers'
 
headers = {'user-agent': 'trang-agent/0.0.1'}
cookies = {'visit-month': 'August'}
  
req = requests.get(url, headers=headers, cookies=cookies)
print (req)
print(req.headers)
print(req.cookies)
