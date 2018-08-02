# Su dung requests de download image va save vao local may

import requests
req = requests.get('https://cms-assets.tutsplus.com/uploads/users/1251/posts/28204/image/Forest_Background_Optimized.jpg', stream=True)
req.raise_for_status()
with open('Forest.jpg', 'wb') as fd:
    for chunk in req.iter_content(chunk_size=50000):
        print('Received a Chunk')
        fd.write(chunk)
