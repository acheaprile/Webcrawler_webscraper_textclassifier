import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.robotparser
import pandas as pd
import tldextract
import time
from time import gmtime
from time import strftime

start_time = time.time()


#Connecting to the site
def web(urladress):
    
    try:
        if 'http' not in urladress:
            web.site = 'http://{}'.format(urladress)
        elif 'http' in urladress[:4]:
            web.site=str(urladress)   
        web.res=requests.get(web.site)
        web.html=web.res.text
        
    except:
        if web.res.status_code!=200:
            print ("*****Connection error with site {}, look for error code {}".format(urladress,str(web.res.status_code)))
            pass
        else:
            pass
    
    return(web.html,web.site)

#Parsing the html
def bf(html):
    
    bf.soup = BeautifulSoup(html, features="html.parser")
    bf.tags=[a["href"] for a in bf.soup.find_all(href=True)]
    return (bf.soup,bf.tags)
 
#Extracting all urls in the page
def geturls(tags):
    
    geturls.allurls=[]
    append=geturls.allurls.append
    
    #Defining which urls within the site are scrappable
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(web(url)[1],"robots.txt"))
    rp.read()
    
    #Extracting all the urls in the main page
    for tag in tags:
 
        if 'http' in tag[:4] and tldextract.extract(tag)[1]==tldextract.extract(url)[1] and str(rp.can_fetch("*",tag))=="True":
            append(tag)
        elif 'http' not in tag[:4] and url in tag and tldextract.extract('http://'+tag)[1]==tldextract.extract(url)[1] and str(rp.can_fetch("*",'http://'+tag))=="True":
            append('http://{}'.format(tag))
        elif 'http' not in tag[:4] and url not in tag and tldextract.extract('http://'+url+tag)[1]==tldextract.extract(url)[1] and str(rp.can_fetch("*",'http://'+url+tag))=="True":
            append('http://{}{}'.format(url,tag))
     
    return (geturls.allurls)


def allurls(mainurls):

    allurls=set([subsite.lower() for site in mainurls for subsite in geturls(bf(web(site)[0])[1])])
      
    return (set(allurls))
        
# Calling the functions and exporting the output to an excel
if __name__== "__main__":
    
    parents=pd.read_csv("{}\parentsites.csv".format(os.getcwd()),header=None)
    
    urlsoutput=pd.DataFrame()
    
    for parentsite in parents.values:
        url=parentsite[0]
        websiteurls=allurls(geturls(bf(web(url)[0])[1]))
        urlsoutput=pd.concat([urlsoutput,pd.DataFrame(websiteurls)])
    
    urlsoutput.to_csv("mainoutput.csv")
    
    print ("My program took", strftime("%H:%M:%S", gmtime(time.time() - start_time)), "to run")