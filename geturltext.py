from bs4 import BeautifulSoup
import requests
import pandas as pd

#Extract the text (if any) from a set of links
def gettext(urls, textlength):
    
    finaltexts=pd.DataFrame()
    
    for u in list(urls.values):
        
        try:
            #Get the website
            res=requests.get(u[1])
            #Get the content of the server’s response
            html=res.text
            #Parsing the HTML
            parsed = BeautifulSoup(html, features="html.parser")
            #Replace the line breaks in the paragraphs
            document=[e.text.replace("\n"," ") for e in parsed.findAll("p")]
            #Extract the text from the url
            if len(" ".join(document))>textlength:
                #We join the paragraphs in the page
                document=pd.Series(" ".join(document))
                url=pd.Series(str(u[1]))
                finaltexts=pd.concat([finaltexts,pd.DataFrame({"text":document, "url":url}).dropna()])
        except:
            pass
    #We remove any text duplicates keeping the first unique url
    finaltexts=finaltexts.drop_duplicates(subset ="text")
    
    return finaltexts

if __name__== "__main__":
    
    file, textlength=str(input("File name: ")),int(input("Minimum number of text char. required:"))
    urls=pd.read_csv("{}.csv".format(file))
    gettext(urls, textlength).to_excel("urltexts.xlsx", encoding='utf-8-sig')
