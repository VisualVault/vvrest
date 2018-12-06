import requests
import json

class IndexField():

	# get all IndexField definitions or pass in query
	def getIndexFields(self,vault,q):
		endpoint = 'indexFields?q=' + q
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# create an index field definition
	def postIndexField(self,vault,label,description,fieldType,queryId,dropDownListId,queryValueField,queryDisplayField,required,defaultValue):
		endpoint = 'indexFields'
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'label':label,'description':description,'fieldType':fieldType,'queryId':queryId,'dropDownListId':dropDownListId,'queryValueField':queryValueField,'queryDisplayField':queryDisplayField,'required':required,'defaultValue':defaultValue}
		r = requests.post(requestUrl,headers=headers,data=payload).json()
		return r

	# update an index field definition
	def putIndexField(self,vault,id,label,description,queryId,dropDownListId,queryValueField,queryDisplayField,required,defaultValue):
		endpoint = 'indexFields/' + id
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'label':label,'description':description,'queryId':queryId,'dropDownListId':dropDownListId,'queryValueField':queryValueField,'queryDisplayField':queryDisplayField,'required':required,'defaultValue':defaultValue}
		r = requests.put(requestUrl,headers=headers,data=payload).json()
		return r

	# relate index field to folder
	def relateIndexField(self,vault,fieldId,folderId):
		endpoint = 'indexFields/' + fieldId + '/folders/' + folderId
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {}
		r = requests.put(requestUrl,headers=headers,data=payload).json()
		return r
