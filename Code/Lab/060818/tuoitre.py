'''
Chuong trinh tai cac bai viet tu https://news.zing.vn
'''

from urllib.parse import urljoin
import requests
import bs4


BASE_URL = 'https://news.zing.vn/'
SOURCE_URL = 'https://news.zing.vn/bao-tuoi-tre-tin-tuc.html'


def get_article_content(url):
    """
    Lay noi dung bai viet tu url
    """
    data = {}
    r = requests.get(url)
    if r.ok:
        s =  bs4.BeautifulSoup(r.content, 'lxml')
        
        title = s.select_one('h1.the-article-title.cms-title')
        data['title'] = title.text.strip() if title else ''
        #print(title.text)
        
        sub_title = s.select_one('p.the-article-summary.cms-desc')
        data['sub_title'] = sub_title.text if sub_title else ''

    return data

def main():
    r = requests.get(SOURCE_URL)
    if r.ok:
       s =  bs4.BeautifulSoup(r.content, 'lxml')
       links = s.select('.article-list.listing-layout article > p > a')
       for a in links:
           print (urljoin(BASE_URL, a.attrs['href']))
    else:
        print('Khong truy cap duoc')
        

if __name__ == '__main__':
    #main()
    print(get_article_content('https://news.zing.vn/nhung-chuyen-cuoi-ra-nuoc-mat-trong-hoi-uc-nguyen-dong-thuc-post838267.html'))
