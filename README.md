# Web Crawler-Scraper and Text Classifier
A web crawler and web scraper that extracts and classifies text pulled from the internet.

## General info
The aim of this project was both to create an effective but simple tool to iteratively navigate and extract links and text from article pages to posteriorly classify these texts into pre-defined categories by using Machine Learning algorithms such as Support Vector Machines (SVMs) or KNN classification.

## Project structure

The project is divided in three independent but connected parts:

- **Web crawler (*maincrwl.py*):** This part intends to extract all the links contained within a domain by iteratively navigating through all the subdomain levels until no new links                                   can be added to the set.
- **Web scraper (*geturltext.py*):**
- **Classifier (*modeltrainingsvm.py* / *modeltrainingdelta.py* and *classifier.py*):**

Here is a diagram of the project's workflow:

![alt text](https://i.ibb.co/7bYPKbk/cl.png)
