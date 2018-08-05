# Tai toan bo trang Wikipedia ve Cong nghe Nano sau do luu vao may

import requests
req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
req.raise_for_status()
with open('Nanotechnology.html', 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
                    fd.write(chunk)
