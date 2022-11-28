from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

types = []
names = []
driver.get('https://kinepolis.fr/?main_section=tous%20les%20films')

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
res = soup.find(id="movie_overview")
card_films = res.find_all("div", class_="movie-container-wrapper")

for a in card_films:
    name = a.find('div', attrs={'class': 'movie-overview-title'})
    typeSeance = a.find('div', attrs={'class': 'movie-container-image'})
    names.append(name.text)
    types.append(typeSeance.text)

df = pd.DataFrame({'Noms': names, 'Types': types})
data_json = df.to_json('films.json')
