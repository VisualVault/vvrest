# *vvrest*
A `Python` REST client library for accessing `VisualVault`.

## requirements
* `python3` and `requests`
```
pip3 install -r requirements.txt
```

## usage
* `pypi` packaging coming soon and docs to follow, so for now add the directory 
`vvrest` into your project and refer to the VVRestTestSuite in the `tests` directory.

For more information on any of the endpoints, data types, or anything referring to the 
`VisualVault` REST API please refer to the `HTTP API` section at <http://developer.visualvault.com>
where each endpoint and there parameters are covered in great detail.

## unittest coverage
```
(venv) rootraider@rootRaider-Oryx-Pro:~/vvrest$ coverage run --source vvrest -m unittest tests/vvrest_test_suite.py ; echo ; coverage report -m
..........................................
----------------------------------------------------------------------
Ran 42 tests in 34.362s

OK

Name                                     Stmts   Miss  Cover   Missing
----------------------------------------------------------------------
vvrest/__init__.py                           0      0   100%
vvrest/constants.py                         30      0   100%
vvrest/services/__init__.py                  0      0   100%
vvrest/services/auth_service.py             21      0   100%
vvrest/services/document_service.py         80      0   100%
vvrest/services/email_service.py            11      0   100%
vvrest/services/file_service.py             29      0   100%
vvrest/services/folder_service.py           73     11    85%   99-104, 192-205
vvrest/services/form_service.py            123     95    23%   21, 34-39, 49-58, 68-75, 83-88, 97-106, 115-120, 130-135, 146-151, 160-165, 174-179, 188-193, 202-207, 216-221, 230-235, 244-248, 257-266, 275-284
vvrest/services/group_service.py            49      1    98%   17
vvrest/services/index_field_service.py      30      0   100%
vvrest/services/site_service.py             35      6    83%   76-90
vvrest/services/user_service.py             37      7    81%   17, 60-74
vvrest/token.py                              5      0   100%
vvrest/utilities.py                          5      0   100%
vvrest/vault.py                             33      0   100%
----------------------------------------------------------------------
TOTAL                                      561    120    79%
```
