import requests
from urllib.parse import urlencode
from urllib.parse import urlparse
import json
from datetime import datetime
import analyse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

API_KEY = 'cad14a9f453224a5a81b5363f341188d'

def get_url(url):
   payload = {'api_key': API_KEY, 'url': url, 'autoparse': 'true', 'country_code': 'us'}
   proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
   return proxy_url

def create_google_url(query, site=''):
   google_dict = {'q': query, 'num': 100,'lr':'lang_zh-CN' }
   if site:
       web = urlparse(site).netloc
       google_dict['as_sitesearch'] = web
       return 'http://www.google.com/search?' + urlencode(google_dict)
   return 'http://www.google.com/search?' + urlencode(google_dict)

def startRequest(url):
    response = requests.get(url)
    print("encoding:"+response.encoding)
    return response

def parseResponse(response):
    #print(response.text)
    pageNb=0
    di = json.loads(response.text)
    #pos = response.meta['pos']
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for result in di['organic_results']:
        title = result['title'] 
        snippet = result['snippet']
        link = result['link']
#        item = {'title': title, 'snippet': snippet, 'link': link, 'position': pos, 'date': dt}
        item = {'title': title, 'snippet': snippet, 'link': link, 'date': dt}
        print("bonjour")
        print("item:"+str(item))
        analyseLink(link)
    next_page = di['pagination']['nextPageUrl']
    if next_page and pageNb<2:
        pageNb=pageNb+1
        print("pageNb:"+str(pageNb))
        proxyUrl=get_url(next_page)
        response=startRequest(proxyUrl)
        parseResponse(response)


def analyseLink(link):
    #response = requests.get(link)
    response = requests.get(link,verify=False)
    if(response.status_code == 200):
        Ana=analyse.AnalyseString(response.text)
        Ana.AnalysHSKProfile()
        print("HSK1:"+str(Ana.HSK1Percent))
        print("HSK2:"+str(Ana.HSK2Percent))
        print("HSK3:"+str(Ana.HSK3Percent))
        print("HSK4:"+str(Ana.HSK4Percent))
        print("HSK5:"+str(Ana.HSK5Percent))
        print("HSK6:"+str(Ana.HSK6Percent))



def main():
    googleUrl=create_google_url("antoine scemama site:.cn")
    proxyUrl=get_url(googleUrl)
    response=startRequest(proxyUrl)
    print("ooooo")
    parseResponse(response)


    print("Hello World!")

if __name__ == "__main__":
    main()

 