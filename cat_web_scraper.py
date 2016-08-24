from bs4 import BeautifulSoup
import requests

url = 'http://www.lolcats.com/page-'

for i in range(1, 3):
    r = requests.get(url + str(i) + '.html')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        for image in soup.find_all('img', 'lolcat'):
            img_name = image['alt']
            img = requests.get('http://www.lolcats.com' + image['src'])
            with open(img_name, 'w') as f:
                f.write(img.content)