import requests
import json

# some invocations that we use in the automated tests; 
# uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

def get_movies_from_tastedive(mname):
    baseurl = 'https://tastedive.com/api/similar'
    params_diction = {}
    params_diction['q'] = mname
    params_diction['type'] = 'movies'
    params_diction['limit'] = 5
    tastedive_res = requests.get(baseurl, params = params_diction)
    print(tastedive_res.url)
    return json.loads(tastedive_res.text)

def extract_movie_titles(dic):
	movie_titles = []
	for item in dic['Similar']['Results']:
		movie_titles.append(item['Name'])

	return movie_titles

def get_related_titles(querymovielist):
    outputlist = []
    for titlelist in querymovielist:
        similarmovielist = get_movies_from_tastedive(titlelist)
        list = extract_movie_titles(similarmovielist)
        for title in list:
            if title not in outputlist:
                outputlist.append(title)
    return outputlist

def get_movie_data(mname):
    baseurl = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = mname
    param['r'] = 'json'
    this_page_cache = requests.get(baseurl, params=param)
    return json.loads(this_page_cache.text)

def get_movie_rating(data):
    rating = 0
    for i in data['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            rating = int(i['Value'][:-1])
            #print(rating)
    return rating 


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]


print("Start----------")

titlelist = get_related_titles(['Forrest Gump', 'Black Panther'])
print(titlelist)

for i in titlelist:
	print('\n--- movie data ---\n')
	moviedata = get_movie_data(i)
	print(json.dumps(moviedata,indent=4))


