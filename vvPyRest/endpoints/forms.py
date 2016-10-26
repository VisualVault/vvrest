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

	# relate form to form
	def relateForm(self,vault,form1,form2):
		endpoint = 'forminstance/' + form1 + '/relateform?relatetoid=' + form2
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers).json()
		return r

	# relate form to doc
	def relateDoc(self,vault,formId,docId):
		endpoint = 'forminstance/' + formId + '/relatedocument?relatetoid=' + docId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers).json()
		return r

	# relate form to project
	def relateProject(self,vault,formId,projectId):
		endpoint = 'forminstance/' + formId + '/relateproject?relatetoid=' + projectId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers).json()
		return r

	# unrelate form to form
	def unrelateForm(self,vault,form1,form2):
		endpoint = 'forminstance/' + form1 + '/unrelateform?relatetoid=' + form2
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers).json()
		return r

	# unrelate form to doc
	def unrelateDoc(self,vault,formId,docId):
		endpoint = 'forminstance/' + formId + '/unrelatedocument?relatetoid=' + docId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers).json()
		return r

	# unrelate form to project
	def unrelateProject(self,vault,formId,projectId):
		endpoint = 'forminstance/' + formId + '/unrelateproject?relatetoid=' + projectId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers).json()
		return r







