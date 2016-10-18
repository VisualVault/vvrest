import requests
import json

class Site():
	# gets all sites
	def getSites(self,vault):
		endpoint = 'sites'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()		
		return r

 	# gets a site by id
	def getSitesUsers(self,vault,id):
		endpoint = 'sites/' + id + '/users'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()		
		return r