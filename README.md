# *vvrest*
A `Python` REST client library for accessing `VisualVault`.

## install
```
pip3 install vvrest
```

## getting started
* The `Vault` class handles `authentication`.
* Services mapping to the different `endpoints` live in the `services` namespace.
For example if one wishes to interact with the `/api/v1/documents` endpoint, 
then import `DocumentService` or for `/api/v1/files` import `FileService`, etc.
* Now credentials need to be defined so `VisualVault` knows who one is.
* `url` is the base url for the instance of `VisualVault` (example below).
NOTE: do not leave a trailing '/' at the end of the `url`.
* `customer_alias` and `database_alias` are the customer and database 
one wishes to connect to.
* `client_id` and `client_secret` can be found on the users page in the
`central admin` section of `VisualVault`. The first `APIKEY` is `client_id`
and the second `APIKEY` is the `client_secret`.
* Each service class in `services` takes an instance of `Vault` as a required parameter.
* The `code example` below demonstrates requesting `documents`.
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
vvrest/constants.py                         31      0   100%
vvrest/services/__init__.py                  0      0   100%
vvrest/services/auth_service.py             27      0   100%
vvrest/services/document_service.py         80      0   100%
vvrest/services/email_service.py            11      0   100%
vvrest/services/file_service.py             25      0   100%
vvrest/services/folder_service.py           73     11    85%   99-104, 192-205
vvrest/services/form_service.py            119     16    87%   178-183, 220-225, 234-238, 250, 268
vvrest/services/group_service.py            49      1    98%   17
vvrest/services/index_field_service.py      30      0   100%
vvrest/services/site_service.py             35      0   100%
vvrest/services/user_service.py             37      1    97%   17
vvrest/token.py                              5      0   100%
vvrest/utilities.py                          8      0   100%
vvrest/vault.py                             34      0   100%
----------------------------------------------------------------------
TOTAL                                      564     29    95%
```
