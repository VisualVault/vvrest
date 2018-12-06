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

	# get document indexfields by documentId
	def getDocumentsFields(self,vault,id):
		endpoint = 'documents/' + id + '/indexfields'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get a document indexfield by documentId and fieldId
	def getDocumentsFieldsId(self,vault,id,fieldId):
		endpoint = 'documents/' + id + '/indexfields/' + fieldId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get index fields of a revision of a document by id and revision id
	def getDocumentsIdRevFields(self,vault,id,revId):
		endpoint = 'documents/' + id + '/revisions/' + revId + '/indexfields'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# get a index field of a revision of a document by id and revision id
	def getDocumentsIdRevFieldsId(self,vault,id,revId,fieldId):
		endpoint = 'documents/' + id + '/revisions/' + revId + '/indexfields/' + fieldId
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.get(requestUrl,headers=headers).json()
		return r

	# update document indexfields
	def updateDocumentFields(self,vault,id,fieldsDict):
		endpoint = 'documents/' + id + '/indexfields'
		requestUrl = vault.baseUrl + endpoint
		fields = {'indexfields':fieldsDict}
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers,data=fields).json()
		return r

	# update a document indexfield
	def updateDocumentFieldsId(self,vault,id,fieldId,value):
		endpoint = 'documents/' + id + '/indexfields/' + fieldId
		requestUrl = vault.baseUrl + endpoint
		fields = {'value':value}
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.put(requestUrl,headers=headers,data=fields).json()
		return r

	# upload a new document	
	def newDoc(self,vault,folderId,docState,name,description,revision,fileName):
		endpoint = 'documents'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'folderId':folderId,'documentState':docState,'name':name,'description':description, 'revision':revision,'allowNoFile':True,'fileLength':0,'fileName':fileName,'indexFields':'{}'}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		return r

	# delete a document
	def deleteDoc(self,vault,id):
		endpoint = 'documents/' + id
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		r = requests.delete(requestUrl,headers=headers).json()
		return r
