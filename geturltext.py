from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from time import gmtime
from time import strftime

def gettext(urls):
    
    finaltexts=pd.DataFrame()
    
    for u in list(urls.values):
        
        try:
            res=requests.get(u[1])
            html=res.text
            soup = BeautifulSoup(html, features="html.parser")
            document=[e.text.replace("\n"," ") for e in soup.findAll("p")]
            if len(" ".join(document))>2000:
                document=pd.Series(" ".join(document[int(len(document)*0.02):int(len(document)*0.9)]))
                url=pd.Series(str(u[1]))
                finaltexts=pd.concat([finaltexts,pd.DataFrame({"text":document, "url":url}).dropna()])
        except:
            pass
    finaltexts=finaltexts.drop_duplicates(subset ="text")
    
    return finaltexts

if __name__== "__main__":
    
    start_time = time.time()
    file=str(input("File name: "))
    urls=pd.read_csv("{}.csv".format(file))
    gettext(urls).to_excel("urltexts.xlsx", encoding='utf-8-sig')
    print ("My program took", strftime("%H:%M:%S", gmtime(time.time() - start_time)), "to run")
