import requests
import json

class SiteService():
	# gets all sites
	def getSites(self,vault):
		endpoint = 'sites'
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()		
		return r

 	# gets a site by id
	def getSitesUsers(self,vault,id):
		endpoint = 'sites/' + id + '/users'
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()		
		return r

	# creates a site
	def postSite(self,vault,name,desc):
		endpoint = 'sites'
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'name': name,'description':desc}
		r = requests.post(requestUrl,headers=headers,data=payload).json()
		return r

	# create user for site
	def postSiteUser(self,vault,siteId,userId,first,last,email,password):
		endpoint = 'sites/' + siteId + '/users'
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'userId':userId, 'firstName':first, 'lastName':last, 'email':email, 'password':password }
		r = requests.post(requestUrl,headers=headers,data=payload).json()
		return r