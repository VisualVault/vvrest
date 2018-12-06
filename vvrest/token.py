# Token Object
class Token():
	# __init__ constructor
	def __init__(self,access_token,token_expiration,refresh_token):
		self.access_token = access_token
		self.token_expiration = token_expiration
		self.refresh_token = refresh_token
