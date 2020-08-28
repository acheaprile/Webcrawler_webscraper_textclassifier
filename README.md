# Web Crawler-Scraper and Text Classifier
A web crawler and web scraper that extracts and classifies text pulled from the internet.

## General info
The aim of this project was both to create an effective but simple tool to iteratively navigate and extract links and text from article pages to posteriorly classify these texts into pre-defined categories by using Machine Learning algorithms such as Support Vector Machines (SVMs) or KNN classification.

Here is a diagram of the project's workflow:

![alt text](https://i.ibb.co/9pL1N6V/cl.png)

## Project structure

The project is divided in three independent but connected parts:

- **Web crawler (*maincrwl.py*):** This part intends to extract (if allowed by the robots.txt) all the links contained within a domain by iteratively navigating through all the subdomain levels until no new links can be added to the set.

- **Web scraper (*geturltext.py*):** It extracts all the documents contained within each one of the links crawled previously.

- **Classifier (*modeltrainingsvm.py* / *modeltrainingdelta.py* and *classifier.py*):** The classifier will learn the classification parameters from the training data and classify the new data pulled by the web scraper into the learnt categories. The text vectorizing is carried out using frequency based methods such as tf-idf or [Delta tf-idf](https://mdsoar.org/handle/11603/12056).

Crawling process diagram:

![alt text](https://i.ibb.co/VpX4pZ6/cl.png)
