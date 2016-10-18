import requests
import json

class Document():
	# get documents by query
	def getDocuments(self,vault,q):
		endpoint = 'documents?q=' + q
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get a document by passing in a documentId
	def getDocumentsId(self,vault,id):
		endpoint = 'documents/' + id
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get all revisions of a document by id
	def getDocumentsIdRev(self,vault,id):
		endpoint = 'documents/' + id + '/revisions'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get a specefic revision of a document by id and revision id
	def getDocumentsIdRevId(self,vault,id,revId):
		endpoint = 'documents/' + id + '/revisions/' + revId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# upload a new document	
	def newDoc(self,vault,folderId,docState,name,description,revision,fileName):
		endpoint = 'documents'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'folderId':folderId,'documentState':docState,'name':name,'description':description, 'revision':revision,'allowNoFile':True,'fileLength':0,'fileName':fileName,'indexFields':'{}'}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		return r

	def deleteDoc(self,vault,id):
		endpoint = 'documents/' + id
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.delete(requestUrl,headers=headers).json()
		return r