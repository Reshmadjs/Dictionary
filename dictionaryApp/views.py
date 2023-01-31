from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.http import HttpResponse
import requests
import json


def home(request):
	if request.method=='POST':
		words=request.POST['word']
		app_id = 'app_id'
		app_key = 'API_KEY'
		language = 'en-gb'
		word_id = words
		url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
		r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
		# here r is HTTTP response
		print("code {}\n".format(r.status_code))
		print("text \n" + r.text)
		# r.text convers rHTTP response into string
		print("json \n" + json.dumps(r.json()))
		

		response = json.loads(r.text)['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
		
		return render(request,'dictionaryApp/word.html',{'response': response,'words':words})
	return render(request,'dictionaryApp/home.html')	





# import  requests
# import json
# # TODO: replace with your own app_id and app_key
# app_id = '<my app_id>'
# app_key = '<my app_key>'
# language = 'en-gb'
# word_id = 'Ace'
# url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
# r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))