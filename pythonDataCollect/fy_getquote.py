import requests
import json


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

querystring = {"region":"US","symbols":"AAPL,ACN,AMZ,GOOG,MSFT"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
print(json.dumps(response.text, indent=2))
