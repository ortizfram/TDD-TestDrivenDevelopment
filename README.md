# TDD-UNIT TESTING
Learn Test Driven Development with Python

👽  Python,Flask, spaCy, pytest, and Selenium.

`❗ENSURES YOU WRITE TESTABLE CODE` & forces you to consider design

## ㊗️ INSTALLATION
- donwload virtualenv

- download [chromeDriver](https://chromedriver.chromium.org/) from chrome or mozilla [geckoDriver](https://github.com/mozilla/geckodriver) from github

- download [spaCY](https://spacy.io/) **processing library**

- download [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)

## ㊗️RULES of TDD
⚪ not allowed to write a piece of code before a failing test 

⚪ write just enough test to fail 

⚪ write just enough code to pass 
## ㊗️ create virtualenv
     mkdir myproject
     cd myproject
     py -3 -m venv venv
### 🟢 activate
     venv\Scripts\activate
## ㊗️ Install dependencies
     pip install spacy selenium pytest flask
     
     #after installation
     python -m spacy download en_core_web_sm
## ㊗️ creation of directories
     mkdir static 
     mkdir templates
     mksdir test
## ㊗️edit setup.py
❗allow us to install current directory as a package
 
     vim setup.py
     
     #inside
     from distutils.core import setup
     from setuptools import find_packages
     
     setup(
               name= 'flaskner',
               version="0.0.1",
               description= "a simple NER API"
     )
     
     #save
     pip install -e . 
