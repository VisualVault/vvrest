import requests
import json

class Form():
	# get all form templates
	def getAllFormTemplates(self,vault):
		endpoint = 'formtemplates'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get form template by id
	def getFormTemplateId(self,vault,formId):
		endpoint = 'formtemplates/' + formId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get form template fields by id
	def getFormTemplateFields(self,vault,formId):
		endpoint = 'formtemplates/' + formId + '/fields'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get form instances of a form template
	def getFormInstances(self,vault,formId):
		endpoint = 'formtemplates/' + formId + '/forms'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get form instances of a form template by search
	def getFormInstancesBySearch(self,vault,formId,q):
		endpoint = 'formtemplates/' + formId + '/forms?q=' + q
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# fill in a form
	def postForm(self,vault,id,fieldsDict):
		endpoint = 'formtemplates/' + id + '/forms'
		requestUrl = vault.baseUrl + endpoint
		fields = fieldsDict
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.post(requestUrl,headers=headers,data=fields).json()
		return r

	# fill in a revision of existing form
	def postRevForm(self,vault,id,revId,fieldsDict):
		endpoint = 'formtemplates/' + id + '/forms/' + revId
		requestUrl = vault.baseUrl + endpoint
		fields = fieldsDict
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.post(requestUrl,headers=headers,data=fields).json()
		return r





