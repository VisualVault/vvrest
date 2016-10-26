import requests
import json

class Group():
	# gets all groups
	def getGroups(self,vault):
		endpoint = 'groups'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()		
		return r