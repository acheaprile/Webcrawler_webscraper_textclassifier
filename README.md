# Web Crawler-Scraper and Text Classifier
A web crawler and web scraper that extracts and classifies text pulled from the internet.

## General info
The aim of this project was both to create an effective but simple tool to iteratively navigate and extract links and text from article pages to posteriorly classify these texts into pre-defined categories by using Machine Learning algorithms such as Support Vector Machines (SVMs).

Here is a diagram of the project's workflow:

![alt text](https://i.ibb.co/9pL1N6V/cl.png)

## Project structure

The project is divided in three independent but connected parts, which must be executed in the following order:

1. **Web crawler (*maincrwl.py*):** This part intends to extract (if allowed by the robots.txt file) all the links contained within a domain by iteratively navigating through all the subdomain levels and storing their links until no new links can be added to the set.

2. **Web scraper (*geturltext.py*):** It aims to extract all the text documents contained within each one of the links previously crawled.

3. **Classifier (*modeltrainingsvm.py* / *modeltrainingdelta.py* and *classifier.py*):** The classifier will learn the classification parameters from the training data and classify the new data pulled by the web scraper into the learnt categories. The text vectorizing is carried out using word frequency based methods such as tf-idf or [Delta tf-idf](https://mdsoar.org/handle/11603/12056).

## Training Data

The training dataset has 10.907 samples and was created by combining both a dataset specifically created for this project (8,681 texts scraped in different websites and manually labelled) and the [BBC News public dataset](https://www.kaggle.com/c/learn-ai-bbc) (2,226 samples). The BBC News dataset represents around 21% of this unique dataset.

## Libraries

The following Python libraries were used in this project:
- Requests
- OS
- BeautifulSoup
- Urlib
- Pandas
- NLTK
- Joblib
- Rake Nltk
- Sklearn
- Matplotlib

## Contact

Please, contact me on my email danielgarciache@gmail.com for any suggestion or question!
Thank you for visiting my GitHub! :)
