import pandas as pd
import nltk
from operator import itemgetter
from joblib import load
import modeltrainingsvm 
from rake_nltk import Rake

def classifier(model, tfidf1, urltoclass, texttoclass,num):
    
    #Classifying new data and collecting ngrams/most frequent ngrams
    classification=[i for i in load(model).predict(tfidf1)]
    
    #Extracting the keywords in the text
    r=Rake(min_length=1, max_length=5)
    rake=[]
    for i in texttoclass:
        r.extract_keywords_from_text(i)
        rake.append(sorted(list(r.get_ranked_phrases_with_scores()),key=itemgetter(0),reverse=True)[0:3])
    
    #Most common n-grams
    fdist=[sorted(list(nltk.FreqDist(nltk.ngrams(nltk.word_tokenize(i),num)).items()), key=itemgetter(1),reverse=True)[0:3] for i in texttoclass]
    
    #Outputting the results
    output=pd.DataFrame({"url":urltoclass,"text":texttoclass,"class":classification, "keywords":rake, "frequent bigrams":fdist})
    
    return output

if __name__== "__main__":

    vect=modeltrainingsvm.vectorizer()
    classifier('{}.joblib'.format(input("Classifier (svm, knn or ensemble):")),vect[1],vect[3],vect[4],float(input("Number of ngrams (>1): "))).to_csv("textclassoutput.csv", encoding='utf-8-sig')
