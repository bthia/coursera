import requests
from bs4 import BeautifulSoup


finurl = "https://finance.yahoo.com/quote/0700.HK?p=0700.HK&.tsrc=fin-srch"
response = requests.request("GET", finurl)
print ("\n\n=====YAHOO FINANCE==================================\n\m")
htmltext = response.text
#print(htmltext)
#print("\n============================================================\n\n")
print("Response")
print(response.status_code)
print("\n================ BeautifulSoup ==========================\n\n")
rel_soup = BeautifulSoup(htmltext, 'html.parser')
print(rel_soup)
rel_soup.span[]