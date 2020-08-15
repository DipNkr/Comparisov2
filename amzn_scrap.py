
from bs4 import BeautifulSoup
import requests




def amzn_data(k):
    
    productName = k
    
    htmlSourceCode = getHtmlSourceCode(productName)
    
    soup = BeautifulSoup(htmlSourceCode, 'html.parser')
    
    a_tags = soup.find_all('a',{'class':'a-link-normal a-text-normal'})
    
    urls = list()
    
    for a in soup.find_all('a',{'class':'a-link-normal a-text-normal'}):
        urls.append('https://www.amazon.in'+a['href'])
        
        
 
        
    return urls[0]



def getHtmlSourceCode(productName):
    
    

    headers = {
        'authority': 'www.amazon.in',
        'cache-control': 'max-age=0',
        'rtt': '450',
        'downlink': '0.5',
        'ect': '3g',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.in/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'session-id=258-2671782-8853057; i18n-prefs=INR; ubid-acbin=260-7184980-9882927; session-token=QNtHcqJ7w3MRmoU8KCEaGIaB0OyKqmT+QdoQJuqPAZkMljfkCMYqMOI7HV+cayz2S7rEf7PJubw5nbNaKuZoOwaSpojTCddLcrejOaBRAR3ZabB+wEoK4ZCfg6kSHyDy077amqsSPmxBd86lbMB/B2Xa6rnIhulD1WXwtLNl9GT9KiHkRAXOpE+Ijn8kOOfe; visitCount=1; csm-hit=tb:s-ZXVXCYG1YQ6YV68FZ6BK^|1597493000099^&t:1597493002582^&adb:adblk_no; session-id-time=2082758401l',
    }

    params = (
        ('k', productName),
        ('ref', 'nb_sb_noss_2'),
    )

    response = requests.get('https://www.amazon.in/s', headers=headers, params=params)

    return response.text
    
    
