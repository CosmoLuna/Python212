import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        items = self.html.find_all('div', class_='Grid__Cell 1/2--phone 1/2--tablet-and-up 1/4--desk')
        for item in items:
            name = item.find("h2").find('span').text
            color = item.find('span', class_='ProductItem__TitleColor').text
            price = item.find('span', class_='ProductItem__Price Price').text
            ref = 'https://www.liewood.com' + item.find('h2', class_='ProductItem__Title u-h7').find('a').get('href')
            self.res.append({
                'name': name,
                'color': color,
                'price': price,
                'ref': ref
            })

    def run(self):
        u = self.url
        for i in range(1, 5):
            self.url = f"{u}{i}"
            self.get_html()
            self.parsing()
            self.save()

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f"{i}. Название: {item['name']}\nЦвет: {item['color']}\nЦена: {item['price']}\nСсылка: {item['ref']}\n\n{'*' * 20}\n\n")
                i += 1
