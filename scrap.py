# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:56:39 2021

@author: Abhishek
"""

from bs4 import BeautifulSoup
import requests 
from csv import writer
url = 'https://housing.com/in/buy/searches/Pskwz0ocdh7q42r5'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('article',class_="css-1nr7r9e")
with open('housing.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['Project Name','Specification(BHK)','Area','Value']
    for list in lists:
        name = list.find('a',class_='css-1lj7uy5').text.replace('\n','')
        area = list.find('div',class_='css-1ty8tu4').text.replace('\n','')
        location = list.find('a',class_='css-16drx2b').text.replace('\n','')
        price = list.find('div',class_='css-18rodr0').text.replace('\n','')
        
        info = [name,area,location,price]
        thewriter.writerow(info)
