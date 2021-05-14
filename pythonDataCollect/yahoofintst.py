import requests
import json

#url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

#querystring = {"q":"tesla","region":"US"}

#headers = {
#    'x-rapidapi-key': "f5af219d20msh604bcf2630c750cp153d04jsn102bf4ea0469",
#    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
#    }

#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
#print("\n\n===========================================================\n\n")


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-timeseries"

querystring = {"symbol":"IBM","period2":"1571590800","period1":"493578000","region":"US"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

x = response.json()
print("Show type\n")
print(type(x))
print ("\n\n==========================================================\n\m")
print("Pretty Text")
print(json.dumps(x, indent=2))
print("\n\n============================================================\n\n")
print("Response")
print(response.status_code)


