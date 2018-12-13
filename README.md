# *vvrest*
A `Python` REST client library for accessing `VisualVault`.

## install
```
pip3 install vvrest
```

## usage
```
from vvrest.vault import Vault
from vvrest.services.document_service import DocumentService

# define credentials
url = 'https://demo.visualvault.com'
customer_alias = 'test_customer'
database_alias = 'test_database'
client_id = '12344b69-cd52-4444-815a-1234ec0fb5ef'
client_secret = 'PouE/GLZ7pjFoqRRyu9L8K3EjTXXdf56sY/FxPaaxxU='

# get vault object (authenticate)
vault = Vault(url, customer_alias, database_alias, client_id, client_secret)

document_service = DocumentService(vault)  # instantiate a service class (DocumentService)
documents = document_service.get_documents("folderPath='/test'")  # request documents
```

* documentation coming soon. 
* refer to the `VVRestTestSuite` in the `tests` directory for more examples.

For more information on any of the endpoints, data types, or anything referring to the 
`VisualVault` REST API please refer to the `HTTP API` section at <http://developer.visualvault.com>
where each endpoint and there parameters are covered in great detail.

## unittest coverage
```
Name                                     Stmts   Miss  Cover   Missing
----------------------------------------------------------------------
vvrest/__init__.py                           0      0   100%
vvrest/constants.py                         30      0   100%
vvrest/services/__init__.py                  0      0   100%
vvrest/services/auth_service.py             21      0   100%
vvrest/services/document_service.py         80      0   100%
vvrest/services/email_service.py            11      0   100%
vvrest/services/file_service.py             25      0   100%
vvrest/services/folder_service.py           73     11    85%   99-104, 192-205
vvrest/services/form_service.py            121     93    23%   21, 34-39, 49-58, 67-72, 80-85, 94-103, 112-117, 127-132, 143-148, 157-162, 171-176, 185-190, 199-204, 213-218, 227-232, 241-245, 254-263, 272-281
vvrest/services/group_service.py            49      1    98%   17
vvrest/services/index_field_service.py      30      0   100%
vvrest/services/site_service.py             35      6    83%   76-90
vvrest/services/user_service.py             37      7    81%   17, 60-74
vvrest/token.py                              5      0   100%
vvrest/utilities.py                          5      0   100%
vvrest/vault.py                             33      0   100%
----------------------------------------------------------------------
TOTAL                                      555    118    79% 
```
