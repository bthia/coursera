import requests
import json


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

querystring = {"region":"US","symbols":"AAPL,ACN,AMZ,GOOG,MSFT"}

headers = {
    'x-rapidapi-key': "f5af219d20msh604bcf2630c750cp153d04jsn102bf4ea0469",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

jsondata = json.loads(response.text)

#print(json.dumps(jsondata, indent=4))

print(json.dumps(jsondata["quoteResponse"],indent=4))