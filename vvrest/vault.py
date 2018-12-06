import requests
import json
import datetime
from .token import Token

# Vault Object
class Vault():
	# __init__ constructor
	def __init__(self,url,customerAlias,databaseAlias,clientId,clientSecret,userName,password):
		self.url = url
		self.customerAlias = customerAlias
		self.databaseAlias = databaseAlias
		self.clientId = clientId
		self.clientSecret = clientSecret
		self.userName = userName
		self.password = password
		self.token = self.getToken(url,clientId,clientSecret,userName,password)
		self.baseUrl = self.getBaseUrl(url,customerAlias,databaseAlias)

	# Access Token
	def getToken(self,url,clientId,clientSecret,userName,password):
		tokenUrl = '/oauth/token'
		requestUrl = url + tokenUrl
		headers = {'Content-Type':'application/json'}
		payload = {'client_id':clientId,'client_secret':clientSecret,'username':userName,'password':password,'grant_type':'password'}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		access_token = r['access_token']
		token_expiration = self.setExpiration(r['expires_in'])
		refresh_token = r['refresh_token']
		token = Token(access_token,token_expiration,refresh_token)
		return token

	# Requests Base Url 
	def getBaseUrl(self,url,customerAlias,databaseAlias):
		baseUrl = url + '/api/v1/' + customerAlias + '/' + databaseAlias + '/'
		return baseUrl

	# Sets UTC time for vault.token.expiration
	def setExpiration(self,expires):
		date = datetime.datetime.utcnow()
		expirationDate = date + datetime.timedelta(seconds=expires)
		return expirationDate

	# void method that refreshes the refresh token from the vault.token object
	def refreshToken(self):
		tokenUrl = '/oauth/token'
		requestUrl = self.url + tokenUrl
		headers = {'Content-Type':'application/json'}
		payload = {'client_id':self.clientId,'client_secret':self.clientSecret,'refresh_token':self.token.refresh_token,'grant_type':'refresh_token'}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		access_token = r['access_token']
		token_expiration = self.setExpiration(r['expires_in'])
		refresh_token = r['refresh_token']
		self.token = Token(access_token,token_expiration,refresh_token)




























