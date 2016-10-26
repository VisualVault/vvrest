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

	# get a group by id
	def getGroup(self,vault,id):
		endpoint = 'groups/' + id
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get a groups users
	def getGroupUsers(self,vault,id):
		endpoint = 'groups/' + id + '/users'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get a user of a group
	def getGroupUser(self,vault,id,userId):
		endpoint = 'groups/' + id + '/users/' + userId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()		
		return r

	# create a new group
	def newGroup(self,vault,name,description,siteId):
		endpoint = 'groups'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'name':name,'description':description, 'siteId':siteId}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		return r

	# updates group
	def updateGroup(self,vault,id,name,description):
		endpoint = 'groups/' + id
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'name':name,'description':description}
		r = requests.put(requestUrl,data=payload,headers=headers).json()
		return r

