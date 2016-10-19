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
