#importing all libraries

import schedule
import time
import webbrowser
import requests
from bs4 import BeautifulSoup
import urllib.request


#Fetching data from website

r=requests.get('https://biharjobsinformer.com/')
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'grid-content'})

first_result=results[0]
link=first_result.find('a')['href']
heading=first_result.find('a').text
web="https://api.telegram.org/bot***********************************/"
web1=web+"sendMessage?chat_id=349041165&text="+str(heading)+str(link)



"""
time.sleep(1)
#Setting cookies of data-id



#Sending through bot

"""	
    
def job():
    urllib.request.urlopen(web1)

schedule.every(10).seconds.do(job)	

while True:
    schedule.run_pending()
    time.sleep(1)
 






  
    
    
    
    
    
    
    
    
    
    
    
    
