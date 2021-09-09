import bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

dwarf_stars_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(dwarf_stars_url)
soup = BeautifulSoup(page.text,"html.parser")
star_table= soup.find_all("table")
temp_list = []
table_rows = star_table[3].find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
star_names = []
distance = []
mass =[]
radius = []


for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
    


df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=["star_name","distance","mass","radius"])
df.to_csv("dwarf_stars.csv")


