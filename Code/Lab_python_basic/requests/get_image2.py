# Truyen tham so trong mot url khi get. Su dung tu khoa params, sau do in ra url de quan sat

import requests
 
query = {'q': 'Forest', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
req = requests.get('https://pixabay.com/en/photos/', params=query)
 
print(req.url)
# returns 'https://pixabay.com/en/photos/?order=popular&min_height=600&q=Forest&min_width=800'
