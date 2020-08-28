import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.robotparser
import pandas as pd
import tldextract

#Sends a request to get a website and its response
def web(urladress):
    
    try:
        #We format the url passed to always include http in the url
        if 'http' not in urladress:
            web.site = 'http://{}'.format(urladress)
        elif 'http' in urladress[:4]:
            web.site=str(urladress)   
        
        #Get the website
        web.res=requests.get(web.site)
        
        #Get the content of the server’s response
        web.html=web.res.text
        
    except:
        #If the server's response is bad, we skip that url
        if web.res.status_code!=200:
            print ("*****Connection error with site {}, look for error code {}".format(urladress,
                   str(web.res.status_code)))
            pass
        else:
            pass
    
    return(web.html,web.site)

#Parsing the HTML
def bf(html):
    
    bf.soup = BeautifulSoup(html, features="html.parser")
    
    #Gets all the links within the parsed url
    bf.tags=[a["href"] for a in bf.soup.find_all(href=True)]
    
    return (bf.soup,bf.tags)
 
#Extracting all urls in the page
def geturls(tags):
    
    geturls.allurls=[]
    append=geturls.allurls.append
    
    #Checking which urls within the domain are scrappable by checking the robots.txt file
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(web(url)[1],"robots.txt"))
    rp.read()
    
    #Extracting all the urls in the link if it has http in the url, the robots.txt file allows us to and
    # if the link belongs to the parent domain
    for tag in tags:
 
        if 'http' in tag[:4] and tldextract.extract(tag)[1]==tldextract.extract(url)[1]\
                    and str(rp.can_fetch("*",tag))=="True":
                        append(tag)
                        
        elif 'http' not in tag[:4]\
                    and url in tag and tldextract.extract('http://'+tag)[1]==tldextract.extract(url)[1]\
                    and str(rp.can_fetch("*",'http://'+tag))=="True":
                        append('http://{}'.format(tag))
                        
        elif 'http' not in tag[:4]\
                    and url not in tag and tldextract.extract('http://'+url+tag)[1]==tldextract.extract(url)[1]\
                    and str(rp.can_fetch("*",'http://'+url+tag))=="True":
                        append('http://{}{}'.format(url,tag))
     
    return (geturls.allurls)


#Extracting iteratively all the links within all the links that have been pulled previously
def allurls(mainurls):

    allurls=set([subsite.lower() for site in mainurls for subsite in geturls(bf(web(site)[0])[1])])
      
    return (set(allurls))
        
# Calling all the functions and exporting the output to an excel
if __name__== "__main__":
    
    parents=pd.read_csv("{}\parentsites.csv".format(os.getcwd()),header=None)
    
    urlsoutput=pd.DataFrame()
    
    for parentsite in parents.values:
        url=parentsite[0]
        websiteurls=allurls(geturls(bf(web(url)[0])[1]))
        urlsoutput=pd.concat([urlsoutput,pd.DataFrame(websiteurls)])
    
    urlsoutput.to_csv("mainoutput.csv")