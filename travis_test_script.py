# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:09:09 2020

@author: rosey
"""

# imports
import requests
from bs4 import BeautifulSoup


# list of urls to scan
url = r'https://www.bbc.co.uk/news'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

results = [i.text for i in soup.find_all('title')][0]
print(results)


# build a new project dir
# git init
# build a new github repo
# hook up travis to your git repo
# git remote add origin url_goes_here!!!
# .gitignore with venv
# activate the venv
# pip freeze to build a requirements.txt
# build the dockerfile
# build the .travis.yml file
# test it - see travis succeed