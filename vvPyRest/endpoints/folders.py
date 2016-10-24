import requests
import json

class Folder():
	# get folder by path
	def getFolderByPath(self,vault,folderPath):
		endpoint = 'folders?folderPath=' + folderPath
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get folder by id
	def getFolderById(self,vault,folderId):
		endpoint = 'folders/' + folderId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get subfolders of a folder by id
	def getSubFolders(self,vault,folderId):
		endpoint = 'folders/' + folderId + '/folders'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get documents of a folder by id
	def getFolderDocs(self,vault,folderId):
		endpoint = 'folders/' + folderId + '/documents'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get indexfields of a folder by id
	def getFolderFields(self,vault,folderId):
		endpoint = 'folders/' + folderId + '/indexfields'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get a indexfield of a folder by id and fieldId
	def getFolderFieldId(self,vault,folderId,fieldId):
		endpoint = 'folders/' + folderId + '/indexfields/' + fieldId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get drop down list indexfield type select options
	def getFolderFieldOptions(self,vault,folderId,fieldId):
		endpoint = 'folders/' + folderId + '/indexfields/' + fieldId + '/selectoptions'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# create a new folder
	def newFolder(self,vault,name,description,allowRevs):
		endpoint = 'folders'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'name':name,'description':description, 'allowRevisions':allowRevs}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		return r

	# create a new sub folder
	def newSubFolder(self,vault,folderId,name,description,allowRevs):
		endpoint = 'folders/' + folderId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'name':name,'description':description, 'allowRevisions':allowRevs}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		return r

	# update folder index field
	def updateFolderField(self,vault,folderId,fieldId,queryId,queryValueField,queryDisplayField,required,defaultValue):
		endpoint = 'folders/' + folderId + '/indexfields/' + fieldId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'dropDownListId':fieldId,'queryId':queryId,'queryValueField':queryValueField,'queryDisplayField':queryDisplayField,'required':required,'defaultValue':defaultValue}
		r = requests.put(requestUrl,data=payload,headers=headers).json()
		return r