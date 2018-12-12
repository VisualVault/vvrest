# imports
from vvrest.vault import Vault
from vvrest.services.document_service import DocumentService
from vvrest.services.email_service import EmailService
from vvrest.services.file_service import FileService
from vvrest.services.folder_service import FolderService
from vvrest.services.form_service import FormService
from vvrest.services.group_service import GroupService
from vvrest.services.index_field_service import IndexFieldService
from vvrest.services.site_service import SiteService
from vvrest.services.user_service import UserService

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
docsRequest = DocumentService(vault)
emailsRequest = EmailService(vault)
filesRequest = FileService(vault)
foldersRequest = FolderService(vault)
formsRequest = FormService(vault)
groupsRequest = GroupService(vault)
indexFieldRequest = IndexFieldService(vault)
sitesRequest = SiteService(vault)
usersRequest = UserService(vault)

# DOCUMENTS
docsRequest.get_documents("folderPath = '/pythonTest'")
docsRequest.get_document('cb80c6cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_revisions('cb80c6cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_revision('cb80c6cc-5995-e611-a6bd-e094676f83f7', 'd7acc9cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_index_fields('cb80c6cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_index_field('cb80c6cc-5995-e611-a6bd-e094676f83f7', '8f191f63-5cc0-e511-a698-e094676f83f7')
docsRequest.get_document_revision_index_fields('cb80c6cc-5995-e611-a6bd-e094676f83f7', 'd7acc9cc-5995-e611-a6bd-e094676f83f7')
docsRequest.get_document_revision_index_field('cb80c6cc-5995-e611-a6bd-e094676f83f7', 'd7acc9cc-5995-e611-a6bd-e094676f83f7', '8f191f63-5cc0-e511-a698-e094676f83f7')
docsRequest.update_document_index_fields('cb80c6cc-5995-e611-a6bd-e094676f83f7', "{'testFIELD': 'changed value', 'testFIELD2': 'new value'}")
docsRequest.update_document_index_field('cb80c6cc-5995-e611-a6bd-e094676f83f7', '8f191f63-5cc0-e511-a698-e094676f83f7', 'indexfield value')
docsRequest.new_document('a31b63b1-5995-e611-a6bd-e094676f83f7', 1, 'documentName', 'description', '0', 'fileName.txt')
docsRequest.delete_document('c267d3c0-5a95-e611-a6bd-e094676f83f7')

# EMAILS
emailsRequest.send_email('test@test.com,test2@aol.com', 'ccRecipient@test.com,cc2@test.com', 'this is the subject',
                         'I am the message body. Hello World!', True, ['726288b1-3c13-e711-a6c8-e094676f83f4'])

# FILES
filesRequest.file_download('03cdf522-5b95-e611-a6bd-e094676f83f7', '/test_docs/test_doc.txt')
filesRequest.file_download_by_search("[testFIELD]='the value'", '/test_docs/test_doc.txt')
filesRequest.file_upload('9908d3ee-5a95-e611-a6bd-e094676f83f7', 'documentName', '1', 'change reason', 'Released',
                         "{'testFIELD': 'the value'}", 'django.txt', '/test_docs/test_doc.txt')

# FOLDERS
foldersRequest.get_folder_search('pythonTest')
foldersRequest.get_folder('a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.get_sub_folders('a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.get_folder_documents('a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.get_folder_index_fields('a31b63b1-5995-e611-a6bd-e094676f83f7')
foldersRequest.get_folder_index_field('a31b63b1-5995-e611-a6bd-e094676f83f7', '586e5e0a-da54-e611-a6b4-e094676f83f7')
foldersRequest.get_folder_index_field_select_options('a31b63b1-5995-e611-a6bd-e094676f83f7', '71065c2b-5dc0-e511-a698-e094676f83f7')
foldersRequest.new_folder('newFolderName', 'new folder description', True)
foldersRequest.new_sub_folder('5213460c-0e9a-e611-a6bd-e094676f83f7', 'subFolderName', 'new sub folder description', True)
foldersRequest.update_folder_index_field('a31b63b1-5995-e611-a6bd-e094676f83f7', '5e1353e2-fa15-e611-a6a6-e094676f83f7', False, 'new default')
foldersRequest.reassign_workflow_relations('39AE342E-0DEE-E611-A6C4-E094676F83F7', '38BE68CD-12EE-E611-A6C4-E094676F83F7', 1, True, False)

# FORMS
formsRequest.get_form_templates("name='TestForm'")
formsRequest.get_form_template('c812d92e-d075-e611-a6b6-e094676f83f7')
formsRequest.get_form_instance('711bc512-39e7-e611-a955-0e991883dbaa', '8ce628f3-1655-e711-a960-dd47132d4eaa', 'fields=Signature')
formsRequest.form_instance_pdf_download('67aeeda5-3155-e711-a6cc-e094676f83f4', 'ce99d471-4055-e711-a6cc-e094676f83f4', '/path/pdfs/a.pdf')
formsRequest.get_form_template_fields('c812d92e-d075-e611-a6b6-e094676f83f7')
formsRequest.get_form_instances('c812d92e-d075-e611-a6b6-e094676f83f7', 'fields=DocumentType')
formsRequest.get_form_instances_search('c812d92e-d075-e611-a6b6-e094676f83f7', "instanceName='rounders-000026'&fields=field1,field2,field3")
formsRequest.create_form_instance('c812d92e-d075-e611-a6b6-e094676f83f7', {'field1': '5', 'field2': True, 'field3': 5})
formsRequest.create_form_instance_revision('c812d92e-d075-e611-a6b6-e094676f83f7', '171a6fc6-9c9b-e611-a6be-e094676f83f7', {'field1': '20', 'field2': False})
formsRequest.relate_form('28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3b112af2-15c9-e511-a699-e094676f83f7')
formsRequest.relate_document('28e9d4e5-27ed-e511-a6a2-e094676f83f7', '03cdf522-5b95-e611-a6bd-e094676f83f7')
formsRequest.relate_project('28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3132ea41-52cb-e511-a699-e094676f83f7')
formsRequest.unrelate_form('28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3b112af2-15c9-e511-a699-e094676f83f7')
formsRequest.unrelate_document('28e9d4e5-27ed-e511-a6a2-e094676f83f7', '03cdf522-5b95-e611-a6bd-e094676f83f7')
formsRequest.unrelate_project('28e9d4e5-27ed-e511-a6a2-e094676f83f7', '3132ea41-52cb-e511-a699-e094676f83f7')
formsRequest.get_embedded_form('db261fc6-fb08-e711-a6c5-e094676f83f7', '823634bb-8552-e611-a6b4-e094676f83f7')
formsRequest.get_related_documents('66a6acba-121b-e711-a6c9-e094676f83f7', 'indexFields=include')
formsRequest.get_related_forms('c7e16f53-c04b-e711-a95f-dd47132d4eaa', "q=[instanceName]='TEST-00000064'")

# GROUPS
groupsRequest.get_groups()
groupsRequest.get_group('abb50248-e8e6-e511-a69e-e094676f83f7')
groupsRequest.get_group_users('abb50248-e8e6-e511-a69e-e094676f83f7')
groupsRequest.get_group_user('abb50248-e8e6-e511-a69e-e094676f83f7', '3fcce17d-7b31-e611-a6ab-e094676f83f7')
groupsRequest.create_group('theGroupName', 'group description', 'b3941561-83bf-e511-a698-e094676f83f7')
groupsRequest.update_group('e8cd0f29-ac9b-e611-a6be-e094676f83f7', 'newGroupName', 'new description')

# IndexFields
indexFieldRequest.get_index_fields("label = 'AAA'")
indexFieldRequest.create_index_field('apiTestLabel', 'test description', 1, False, 'default value')
indexFieldRequest.update_index_field('61f55ae3-36cd-e611-a6c1-e094676f83f7', 'newApiTestLabel', 'new test description',
                                     '00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000', '',
                                     '', True, '&&new default value&&')
indexFieldRequest.relate_index_field_to_folder('61f55ae3-36cd-e611-a6c1-e094676f83f7', 'c71b45c5-0ecd-e611-a6c1-e094676f83f7')

# SITES
sitesRequest.get_sites()
sitesRequest.get_site('61f55ae3-36cd-e611-a6c1-e094676f83f7')
sitesRequest.get_site_users('b3941561-83bf-e511-a698-e094676f83f7')
sitesRequest.create_site('testing3', 'test desc')

# USERS
usersRequest.get_users("userid='test@test.com'")
usersRequest.get_user('7280297a-5519-e611-a6a8-e094676f83f7')
usersRequest.get_user_web_token('65dcb4a6-fdb3-e511-a694-e094676f83f7')
usersRequest.update_user('5aecb42d-ffc8-e511-a699-e094676f83f7', {'enabled': True, 'lastName': 'new name'})
