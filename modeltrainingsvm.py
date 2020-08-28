import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump
import scikitplot as skplt
import matplotlib.pyplot as plt
import seaborn as sn

def vectorizer():
    
    #Read all the different files that are going to be needed    
        #Training Data
    trainingdata=pd.read_csv("trainingdata.csv", engine='python')
    trainingtexts=[str(i) for i in trainingdata["text"]]
    categories=[str(i) for i in trainingdata["category"]]
        #New data to classify (we used the texts extracted with the scraper)
    inputtexts=pd.read_excel("urltexts.xlsx", encoding='utf-8-sig')
    texttoclass=[i for i in inputtexts["text"]]
    urltoclass=[i for i in inputtexts["url"]]

    #Vectorizing and appliying tfidf on all the documents
    tfidf_vectorizer=TfidfVectorizer(use_idf=True,stop_words="english")
    fitted_vectorizer=tfidf_vectorizer.fit(trainingtexts)
        #Vectorizing training data
    tfidf=fitted_vectorizer.transform(trainingtexts)
        #Vectorizing new data from the scraper to predict
    tfidf1=fitted_vectorizer.transform(texttoclass).todense()
    
    return(tfidf,tfidf1,categories,urltoclass,texttoclass)
    
def modeltraining(data,labels,trsize):

   #Feeding training data into the classification model
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto', probability=True)
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=trsize, random_state=43)
    mod=BaggingClassifier(base_estimator=SVM,n_estimators=5, random_state=43).fit(X_train, y_train)
    #We save the parameters of the model trained in a .joblib file to use them later
    dump(mod, 'svm.joblib')
    
    #Testing the classifier
    y_pred=mod.predict(X_test)
    #We print the performance report and metrics of the model
    print(confusion_matrix(y_test, y_pred))
    sn.heatmap(confusion_matrix(y_test, y_pred), xticklabels=set(labels), yticklabels=set(labels))
    skplt.metrics.plot_confusion_matrix(y_test, y_pred, normalize=True, figsize=(10,10))
    plt.show()
    
    print(classification_report(y_test, y_pred))
    print (set(labels))
    y_proba=mod.predict_proba(X_test)
    skplt.metrics.plot_roc(y_test,y_proba)
    plt.show()

if __name__== "__main__":
    v=vectorizer()
    modeltraining(v[0],v[2],float(input("Size of the test data (float in the (0, 1) range): ")))
