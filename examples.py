# imports
# from vvrest import *
from vvrest import Vault
from vvrest import Document
from vvrest import Email
from vvrest import File
from vvrest import Folder
from vvrest import Form
from vvrest import Group
from vvrest import IndexField
from vvrest import Site
from vvrest import User

# Declare your constants as strings here for authorization to request your access token.
# This token will automatically be requested and hard coded into the helper methods throughout the application.
# For the url variable, do not end url with a '/'.
# i.e. for using https://demo.visualvault.com let url = 'https://demo.visualvault.com'.
# customerAlias and databaseAlias are the customer and database you would like to connect to.
# clientId and clientSecret can be found in central admin on your instance of VisualVault under your user name.
# The first APIKEY is the clientId and the second APIKEY is the clientSecret.
# userName is your user name and password is your password.

# credentials
url = 'https://demo.visualvault.com'
customerAlias = 'testCustomer'
databaseAlias = 'testDatabase'
clientId = '58cd2149-a78d-4623-80e8-9fff4fb66679'
clientSecret = 'khN18YAZPe6F3Z0tc2W0HXCb487jm0wgwe6kNffUNf0='

# get VaultObject
vault = Vault(url, customerAlias, databaseAlias, clientId, clientSecret)

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

# DOCUMENTS
docsRequest.delete_document(vault, 'c267d3c0-5a95-e611-a6bd-e094676f83f7')
docsRequest.get_documents(vault, "folderPath = '/pythonTest'")
docsRequest.get_document_by_id(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_revisions_by_id(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_revision_by_revision_id(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7', 'd7acc9cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_index_fields(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_index_fields_by_field_id(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7', '8f191f63-5cc0-e511-a698-e094676f83f7')
docsRequest.get_document_revision_index_fields(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7', 'd7acc9cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_revision_fields_by_field_id(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7', 'd7acc9cc-5995-e611-a6bd-e094676f83f7', '8f191f63-5cc0-e511-a698-e094676f83f7')
docsRequest.update_document_index_fields(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7', "{'testFIELD': 'changed value', 'testFIELD2': 'new value'}")
docsRequest.update_document_index_field(vault, 'cb80c6cc-5995-e611-a6bd-e094676f83f7', '8f191f63-5cc0-e511-a698-e094676f83f7', 'indexfield value')
docsRequest.new_document(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7', 1, 'documentName', 'description', '0', 'fileName.txt')

# EMAILS
emailsRequest.sendEmail(vault, 'test@test.com,test2@aol.com', 'ccRecipient@test.com,cc2@test.com',
                        'this is the subject', 'I am the message body. Hello World!', True, ['726288b1-3c13-e711-a6c8-e094676f83f4'])

# FILES
filesRequest.fileDownload(vault, '03cdf522-5b95-e611-a6bd-e094676f83f7', 'VISUALVAULT\docs\pythonTest\django.txt')
filesRequest.fileDownloadBySearch(vault, '[testFIELD]=\'the value\'', 'VISUALVAULT\docs\pythonTest\django2.txt')
filesRequest.fileUpload(vault, '9908d3ee-5a95-e611-a6bd-e094676f83f7', 'documentName', '1', 'change reason',
                        'Released', '{\'testFIELD\':\'the value\'}', 'django.txt', 'VISUALVAULT\docs\django.txt')

# FOLDERS
foldersRequest.getFolderByPath(vault, 'pythonTest')
foldersRequest.getFolderById(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.getSubFolders(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.getFolderDocs(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.getFolderFields(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.getFolderFieldId(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7', '586e5e0a-da54-e611-a6b4-e094676f83f7')
foldersRequest.getFolderFieldOptions(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7', '71065c2b-5dc0-e511-a698-e094676f83f7')
foldersRequest.newFolder(vault, 'newFolderName', 'new folder description', True)
foldersRequest.newSubFolder(vault, '5213460c-0e9a-e611-a6bd-e094676f83f7', 'subFolderName', 'new sub folder description', True)
foldersRequest.updateFolderField(vault, 'a31b63b1-5995-e611-a6bd-e094676f83f7', '5e1353e2-fa15-e611-a6a6-e094676f83f7',
                                 '00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000', '', '', False, 'new default')
foldersRequest.reassignWorkflowRelations(vault, '39AE342E-0DEE-E611-A6C4-E094676F83F7', '38BE68CD-12EE-E611-A6C4-E094676F83F7', 1, True, False)

# FORMS
formsRequest.getAllFormTemplates(vault, 'name = \'TestForm\'')
formsRequest.getFormTemplateId(vault, 'c812d92e-d075-e611-a6b6-e094676f83f7')
formsRequest.getFormTemplateForm(vault, '711bc512-39e7-e611-a955-0e991883dbaa', '8ce628f3-1655-e711-a960-dd47132d4eaa', 'fields=Signature')
formsRequest.getFormPDF(vault, '67aeeda5-3155-e711-a6cc-e094676f83f4', 'ce99d471-4055-e711-a6cc-e094676f83f4', '/path/pdfs/a.pdf')
formsRequest.getFormTemplateFields(vault, 'c812d92e-d075-e611-a6b6-e094676f83f7')
formsRequest.getFormInstances(vault, 'c812d92e-d075-e611-a6b6-e094676f83f7', 'fields=DocumentType')
formsRequest.getFormInstancesBySearch(vault, 'c812d92e-d075-e611-a6b6-e094676f83f7', 'instanceName=\'rounders-000026\'&fields=field1,field2,field3')
formsRequest.postForm(vault, 'c812d92e-d075-e611-a6b6-e094676f83f7', {'field1': '5', 'field2': True, 'field3': 5})
formsRequest.postRevForm(vault, 'c812d92e-d075-e611-a6b6-e094676f83f7', '171a6fc6-9c9b-e611-a6be-e094676f83f7', {'field1': '20', 'field2': False})
formsRequest.relateForm(vault, '28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3b112af2-15c9-e511-a699-e094676f83f7')
formsRequest.relateDoc(vault, '28e9d4e5-27ed-e511-a6a2-e094676f83f7', '03cdf522-5b95-e611-a6bd-e094676f83f7')
formsRequest.relateProject(vault, '28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3132ea41-52cb-e511-a699-e094676f83f7')
formsRequest.unrelateForm(vault, '28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3b112af2-15c9-e511-a699-e094676f83f7')
formsRequest.unrelateDoc(vault, '28e9d4e5-27ed-e511-a6a2-e094676f83f7', '03cdf522-5b95-e611-a6bd-e094676f83f7')
formsRequest.unrelateProject(vault, '28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3132ea41-52cb-e511-a699-e094676f83f7')
formsRequest.embedForm(vault, 'db261fc6-fb08-e711-a6c5-e094676f83f7', '823634bb-8552-e611-a6b4-e094676f83f7')
formsRequest.getRelatedDocs(vault, '66a6acba-121b-e711-a6c9-e094676f83f7', 'indexFields=include')
formsRequest.getRelatedForms(vault, 'c7e16f53-c04b-e711-a95f-dd47132d4eaa', "q=[instanceName]='TEST-00000064'")

# GROUPS
groupsRequest.getGroups(vault, '')
groupsRequest.getGroup(vault, 'abb50248-e8e6-e511-a69e-e094676f83f7')
groupsRequest.getGroupUsers(vault, 'abb50248-e8e6-e511-a69e-e094676f83f7')
groupsRequest.getGroupUser(vault, 'abb50248-e8e6-e511-a69e-e094676f83f7', '3fcce17d-7b31-e611-a6ab-e094676f83f7')
groupsRequest.newGroup(vault, 'theGroupName', 'group description', 'b3941561-83bf-e511-a698-e094676f83f7')
groupsRequest.updateGroup(vault, 'e8cd0f29-ac9b-e611-a6be-e094676f83f7', 'newGroupName', 'new description')

# IndexFields
indexFieldRequest.getIndexFields(vault, "label = 'AAA'")
indexFieldRequest.postIndexField(vault, 'apiTestLabel', 'test description', 1, '00000000-0000-0000-0000-000000000000',
                                 '00000000-0000-0000-0000-000000000000', '', '', False, '&&default value&&')
indexFieldRequest.putIndexField(vault, '61f55ae3-36cd-e611-a6c1-e094676f83f7', 'newApiTestLabel', 'new test description',
                                '00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000', '', '', True, '&&new default value&&')
indexFieldRequest.relateIndexField(vault, '61f55ae3-36cd-e611-a6c1-e094676f83f7', 'c71b45c5-0ecd-e611-a6c1-e094676f83f7')

# SITES
sitesRequest.getSites(vault)
sitesRequest.getSitesUsers(vault, 'b3941561-83bf-e511-a698-e094676f83f7')
sitesRequest.postSite(vault, 'testing3', 'test desc')
sitesRequest.postSiteUser(vault, '60c10915-2c25-e711-a95c-dd47132d4e4a', 'test.jones2', 'firstName', 'lastName', 'jimmy@gmail.com', 'password')

# USERS
usersRequest.getUsers(vault, "userid='test@test.com'")
usersRequest.getUser(vault, '7280297a-5519-e611-a6a8-e094676f83f7')
usersRequest.getUserToken(vault, '65dcb4a6-fdb3-e511-a694-e094676f83f7')
usersRequest.postUser(vault, '3adcb4a6-fdb3-e511-a694-e094676f83f7', 'user.py', 'python', 'user', 'test@aol.com', 'p')
usersRequest.putUser(vault, '5aecb42d-ffc8-e511-a699-e094676f83f7', {'enabled': True, 'lastname': 'new name'})
