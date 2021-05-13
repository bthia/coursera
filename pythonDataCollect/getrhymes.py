# import statements for necessary Python modules

import requests


def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url


def get_rhymes(word):
   baseurl = "https://api.datamuse.com/words"
   params_diction = {} # Set up an empty dictionary for query parameters
   params_diction["rel_rhy"] = word
   params_diction["max"] = "6" # get at most 3 results
   print("requestURL: ", requestURL(baseurl, params=params_diction))
   # print("reqest.requestURL: ", requests.requestURL(baseurl, params=params_diction))
   resp = requests.get(baseurl, params=params_diction)
   
   # return the top three words
   word_ds = resp.json()

   return [d['word'] for d in word_ds]
#   return resp.json() # Return a python object (a list of dictionaries in this case)

print(get_rhymes("democracy"))