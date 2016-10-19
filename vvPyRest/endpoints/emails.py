import requests
import json

class Email():
	# send an email through VV
	def sendEmail(self,vault,recipient,ccRecipient,subject,body):
		endpoint = 'emails'
		requestUrl = vault.baseUrl + endpoint
		headers = {'Authorization':'Bearer ' + vault.token.access_token}
		payload = {'recipients':recipient,'ccrecipients':ccRecipient,'subject':subject,'body':body}
		r = requests.post(requestUrl,data=payload,headers=headers).json()
		return r