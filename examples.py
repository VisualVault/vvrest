# from vvPyRest import *

from vvPyRest import Vault
from vvPyRest import Document
from vvPyRest import Email
from vvPyRest import File
from vvPyRest import Folder
from vvPyRest import Form
from vvPyRest import Group
from vvPyRest import IndexField
from vvPyRest import Site
from vvPyRest import User

# Declare your constants as strings here for authorzation to request your access token.
# This token will automatically be requested and hard coded into the helper methods throughout the application. 
# For the url variable, do not end url with a '/'.
# i.e. for using https://demo.visualvault.com let url = 'https://demo.visualvault.com'.
# customerAlias and databaseAlias are the customer and database you would like to connect to.
# clientId and clientSecret can be found in the central admin section on your instance of visual vault under your user name. 
# The first APIKEY is the clientId and the second APIKEY is the clientSecret. 
# userName is your user name and password is your password. 

# credentials
url = 'https://demo.visualvault.com'
customerAlias = 'testCustomer'
databaseAlias = 'testDatabase'
clientId = '58cd2149-a78d-4623-80e8-9fff4fb66679'
clientSecret = 'khN18YAZPe6F3Z0tc2W0HXCb487jm0wgwe6kNffUNf0='
userName = 'test.user'
password = 'password'

# get VaultObject
vault = Vault(url,customerAlias,databaseAlias,clientId,clientSecret,userName,password)

# vault request objects
docsRequest = Document()
emailsRequest = Email()
filesRequest = File()
foldersRequest = Folder()
formsRequest = Form()
groupsRequest = Group()
indexFieldRequest = IndexField()
sitesRequest = Site()
usersRequest = User()

##################### REQUESTS ##########################

# DOCUMENTS

print docsRequest.deleteDoc(vault,'c267d3c0-5a95-e611-a6bd-e094676f83f7')
print docsRequest.getDocuments(vault,'folderPath = \'/pythonTest\'')
print docsRequest.getDocumentsId(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7')
print docsRequest.getDocumentsIdRev(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7')
print docsRequest.getDocumentsIdRevId(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7','d7acc9cc-5995-e611-a6bd-e094676f83f7')
print docsRequest.getDocumentsFields(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7')
print docsRequest.getDocumentsFieldsId(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7','8f191f63-5cc0-e511-a698-e094676f83f7')
print docsRequest.getDocumentsIdRevFields(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7','d7acc9cc-5995-e611-a6bd-e094676f83f7')
print docsRequest.getDocumentsIdRevFieldsId(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7','d7acc9cc-5995-e611-a6bd-e094676f83f7','8f191f63-5cc0-e511-a698-e094676f83f7')
print docsRequest.updateDocumentFields(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7','{\'testFIELD\':\'changed value\',\'testFIELD2\':\'new value\'}')
print docsRequest.updateDocumentFieldsId(vault,'cb80c6cc-5995-e611-a6bd-e094676f83f7','8f191f63-5cc0-e511-a698-e094676f83f7','indexfield value')
print docsRequest.newDoc(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7',1,'documentName','description','0','fileName.txt')

# EMAILS

print emailsRequest.sendEmail(vault,'test@test.com,test2@aol.com','ccRecipient@test.com,cc2@test.com','this is the subject','I am the message body. Hello World!')

# FILES

print filesRequest.fileDownload(vault,'03cdf522-5b95-e611-a6bd-e094676f83f7','VISUALVAULT\docs\pythonTest\django.txt')
print filesRequest.fileDownloadBySearch(vault,'[testFIELD]=\'the value\'','VISUALVAULT\docs\pythonTest\django2.txt')
print filesRequest.fileUpload(vault,'9908d3ee-5a95-e611-a6bd-e094676f83f7','documentName','1','change reason','Released','{\'testFIELD\':\'the value\'}','django.txt','VISUALVAULT\docs\django.txt')

# FOLDERS

print foldersRequest.getFolderByPath(vault,'pythonTest')
print foldersRequest.getFolderById(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7')
print foldersRequest.getSubFolders(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7')
print foldersRequest.getFolderDocs(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7')
print foldersRequest.getFolderFields(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7')
print foldersRequest.getFolderFieldId(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7','586e5e0a-da54-e611-a6b4-e094676f83f7')
print foldersRequest.getFolderFieldOptions(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7','71065c2b-5dc0-e511-a698-e094676f83f7')
print foldersRequest.newFolder(vault,'newFolderName','new folder description',True)
print foldersRequest.newSubFolder(vault,'5213460c-0e9a-e611-a6bd-e094676f83f7','subFolderName','new sub folder description',True)
print foldersRequest.updateFolderField(vault,'a31b63b1-5995-e611-a6bd-e094676f83f7','5e1353e2-fa15-e611-a6a6-e094676f83f7','00000000-0000-0000-0000-000000000000','','',False,'new default')

# FORMS

print formsRequest.getAllFormTemplates(vault)
print formsRequest.getFormTemplateId(vault,'c812d92e-d075-e611-a6b6-e094676f83f7')
print formsRequest.getFormTemplateFields(vault,'c812d92e-d075-e611-a6b6-e094676f83f7')
print formsRequest.getFormInstances(vault,'c812d92e-d075-e611-a6b6-e094676f83f7')
print formsRequest.getFormInstancesBySearch(vault,'c812d92e-d075-e611-a6b6-e094676f83f7','instanceName=\'rounders-000026\'&fields=field1,field2,field3')
print formsRequest.postForm(vault,'c812d92e-d075-e611-a6b6-e094676f83f7',{'field1':'5','field2':True,'field3':5})
print formsRequest.postRevForm(vault,'c812d92e-d075-e611-a6b6-e094676f83f7','171a6fc6-9c9b-e611-a6be-e094676f83f7',{'field1':'20','field2':False})
print formsRequest.relateForm(vault,'28e9d4e5-27ed-e511-a6a2-e094676f83f7','3b112af2-15c9-e511-a699-e094676f83f7')
print formsRequest.relateDoc(vault,'28e9d4e5-27ed-e511-a6a2-e094676f83f7','03cdf522-5b95-e611-a6bd-e094676f83f7')
print formsRequest.relateProject(vault,'28e9d4e5-27ed-e511-a6a2-e094676f83f7','3132ea41-52cb-e511-a699-e094676f83f7')
print formsRequest.unrelateForm(vault,'28e9d4e5-27ed-e511-a6a2-e094676f83f7','3b112af2-15c9-e511-a699-e094676f83f7')
print formsRequest.unrelateDoc(vault,'28e9d4e5-27ed-e511-a6a2-e094676f83f7','03cdf522-5b95-e611-a6bd-e094676f83f7')
print formsRequest.unrelateProject(vault,'28e9d4e5-27ed-e511-a6a2-e094676f83f7','3132ea41-52cb-e511-a699-e094676f83f7')

# GROUPS
print groupsRequest.getGroups(vault)
print groupsRequest.getGroup(vault,'abb50248-e8e6-e511-a69e-e094676f83f7')
print groupsRequest.getGroupUsers(vault,'abb50248-e8e6-e511-a69e-e094676f83f7')
print groupsRequest.getGroupUser(vault,'abb50248-e8e6-e511-a69e-e094676f83f7','3fcce17d-7b31-e611-a6ab-e094676f83f7')
print groupsRequest.newGroup(vault,'theGroupName','group description','b3941561-83bf-e511-a698-e094676f83f7')
print groupsRequest.updateGroup(vault,'e8cd0f29-ac9b-e611-a6be-e094676f83f7','newGroupName','new description')

# IndexFields
print indexFieldRequest.getIndexFields(vault,"label = 'AAA'")

# SITES

print sitesRequest.getSites(vault)
print sitesRequest.getSitesUsers(vault,'b3941561-83bf-e511-a698-e094676f83f7')

# USERS

print usersRequest.getUsers(vault)












