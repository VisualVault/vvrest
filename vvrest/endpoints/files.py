import requests
import json

class File():
	# download a file by revision id to local file system
	def fileDownload(self,vault,id,filePath):
		endpoint = 'files/' + id
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers,stream=True)	
		file = open(filePath,'wb')
		data = r.raw.read()
		file.write(data)	
		return r

	# download a file by query to local file system
	def fileDownloadBySearch(self,vault,q,filePath):
		endpoint = 'files/?q=' + q
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers,stream=True)	
		file = open(filePath,'wb')
		data = r.raw.read()
		file.write(data)	
		return r

	# upload a file
	def fileUpload(self,vault,docId,name,revision,changeReason,checkInState,indexFields,fileName,filePath):
		endpoint = 'files'
		requestUrl = vault.base_url + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		params = {'documentId':docId,'name':name,'revision':revision,'changeReason':changeReason,'checkInDocumentState':checkInState, 'indexFields':indexFields, 'fileName':fileName}
		files = {'fileUpload': (fileName, open(filePath, 'rb'), 'application/octet-stream')}
		r = requests.post(requestUrl,headers=headers,data=params,files=files).json()
		return r

