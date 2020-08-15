
from bs4 import BeautifulSoup
import requests



def helloWorld(p):
    
    productName = p
    
    htmlSourceCode = getHtmlSourceCode(productName)
    
    soup = BeautifulSoup(htmlSourceCode, 'html.parser')
    
    a_tags = soup.find_all('a',{'class':'_2cLu-l'})
    
    urls = list()
    
    for a in soup.find_all('a',{'class':'_2cLu-l'}):
        urls.append('https://www.flipkart.com'+a['href'])
        
        
    for a in soup.find_all('a',{'class':'_31qSD5'}):
        urls.append('https://www.flipkart.com'+a['href'])
        
    
    for a in soup.find_all('a',{'class':'_3dqZjq'}):
        urls.append('https://www.flipkart.com'+a['href'])
        
        
    """products = list()
    for url in urls:
        product = dict()
        page_soup = BeautifulSoup(requests.get(url).text, 'html.parser')

        name = page_soup.find('h1', {'class':'_9E25nV'})
        product['name'] = name.text

        price = page_soup.find('div', {'class':'_1vC4OE _3qQ9m1'})
        product['price'] = price.text

        link=url
        product['URL']=link


        ratingsAndReviews = page_soup.find('span', {'class':'_38sUEc'})

        if ratingsAndReviews is None:
            product['ratingsAndReviews'] = '0 ratings & 0 reviews'
        else:
            product['ratingsAndReviews'] = ratingsAndReviews.text

        products.append(product)

        break"""
    for url in urls:
        return url
        break



def getHtmlSourceCode(productName):
    
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    params = (
        ('q', productName),
        ('otracker', 'search'),
        ('otracker1', 'search'),
        ('marketplace', 'FLIPKART'),
        ('as-show', 'on'),
        ('as', 'off'),
        ('as-pos', '1'),
        ('as-type', 'HISTORY'),
    )

    response = requests.get('https://www.flipkart.com/search', headers=headers, params=params)

    return response.text
