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