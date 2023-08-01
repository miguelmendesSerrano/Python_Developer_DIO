""" Desenvolvendo um Web Scraping """

from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br').content

soup = BeautifulSoup(site, 'html.parser')
# exemplos de extração de infos do site
print(soup.title.string)

print(soup.p.string)

print(soup.a.string)
# busca com o modo find
temp = soup.find('span', class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")
print(temp.string)
