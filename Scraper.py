from tkinter import*
import requests

import re



from bs4 import BeautifulSoup
global hit
hit = []
FW = ["fraud"]
givenData = ["theranos","null","null","null"]
def webScraper(givenData,FW):
    company_name = givenData[0]
    company_url = givenData[1]
    company_industry = givenData[2]
    company_location = givenData[3]
    
    

    

    BASE_URL = 'http://www.google.com/search?q='+'"'+company_name+'"+'
    
    dat_file = (r'words')

    for i in FW:
        
       
        url = BASE_URL+'"'+i+'"'
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        line_count = 1
        
        
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }
        url = 'https://search.brave.com/search?q="'+company_name+'"'+'"'+i+'"&source=web'
        #print(url)
        r = requests.get(url,headers=headers,verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        print(r.status_code)
        
        hit.append(soup.encode('utf-8', errors = 'ignore'))
        
        
        #print(hit)
def regEx(list):
    listStr = list[0]
    #listStr = ' '.join(map(str,list))
    prog = re.compile(r".+")
    #prog = re.compile(r"(h)")
    x = re.findall(prog,hit[0].decode('utf-8', errors= 'ignore'))
    print(hit)       
webScraper(givenData,FW)
regEx(hit)
#hit_brief = 


