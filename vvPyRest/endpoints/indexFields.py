import requests
import json

class IndexField():

	# get all IndexField definitions or pass in query
	def getIndexFields(self,vault,q):
		endpoint = 'indexFields?q=' + q
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r