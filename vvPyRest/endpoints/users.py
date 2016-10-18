import requests
import json

class User():
	# gets all users
	def getUsers(self,vault):
		endpoint = 'users'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()		
		return r
