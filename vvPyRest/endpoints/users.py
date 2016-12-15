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

	# creates a user
	def postUser(self,vault,siteId,userId,fName,lName,email,password):
		endpoint = 'users?siteId='
		requestUrl = vault.baseUrl + endpoint + siteId
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'userId':userId,'firstName':fName,'lastName':lName,'emailaddress':email,'password':password}
		r = requests.post(requestUrl,headers=headers,data=payload).json()
		return r