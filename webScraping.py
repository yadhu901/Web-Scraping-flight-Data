
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:40:32 2019
@author: yadhunandsrinivasan
"""

#import packages required for webscraping and loading json data into a df
import json
import urllib
import requests
import pandas as pd
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup


#url to scrap data from - 'https://www.flysfo.com/flight-info/flight-status'
#check to see if any network calls are made to fetch the data, by inspecting the web page
#If yes then use the network call to scrape data

url = 'https://databroker.flysfohosting.net/api/flights-sortable/full/json?_=1564955683864'

#request to url
re = requests.get(url, headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},verify=False).text



#parse to a BeautifulSoup Object
soup = BeautifulSoup(re, 'lxml')
body=soup.find_all('p')

# get the data between HTML tags
inner_contents = soup.find('p').contents

contents=inner_contents[0]

#clean the data
replace_string='aaData'

jsond_clean=contents.replace(replace_string,"")

replace_string=r'{"":'
print(replace_string)
jsond_clean_1=jsond_clean.replace(replace_string,"")
jsond_clean_1=jsond_clean_1[:-1]



#print(jsond_clean_1)

#load the data to JSON object
jsonD = json.dumps(jsond_clean_1)
d1=json.loads(jsond_clean_1)

#create a df 
df = pd.DataFrame.from_dict(d1, orient='columns')

#load the df to an excel
df.to_excel(r'/Users/yadhunandsrinivasan/Desktop/data/flights.xlsx')

