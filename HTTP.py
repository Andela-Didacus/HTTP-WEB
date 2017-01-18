import requests                                     #imports the requests module to access GET, PUT, POST, DELETE functions
import json                                         #import json to allow viewing of data written in javascript notation

api_key = 'b56261c81aa38036'                        #API key for for identification with the API program at api.fullcontact.com

url = "https://api.fullcontact.com/v2/person.json"  #the url from which the apis are retrieved

def find_person(**kwargs):                          #function receives person's email as a parameter to search for details 
  if 'apiKey' not in kwargs:                        #assigns api key as one of the parameters
    kwargs['apiKey'] = api_key

  r = requests.get(url, params=kwargs)              #get function retrieves the data using the email as a parameter
  return json.loads(r.text)                         #returns the data 



print find_person(email="mike@yahoo.com")
