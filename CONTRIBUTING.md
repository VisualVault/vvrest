## contributing to *vvrest*
this file serves as a process to manage contribution guidelines for the 
[vvrest python package](https://pypi.org/project/vvrest/).

### developer expectations
when contributing to `vvrest`, developers are expected to:
* submit work in `python3` (python2 is not supported)
* adhere to [PEP8](https://www.python.org/dev/peps/pep-0008/)
* follow the [gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow
* only submit [Pull Requests](https://help.github.com/articles/creating-a-pull-request/) 
(PRs) with a fully passing test suite
* submit `test` coverage for features/issues when applicable.

### environment setup
set up a [python virtual environment](https://docs.python.org/3/library/venv.html#module-venv) 
(venv) at the root directory of the project:
```commandline
python3 -m venv ./venv
pip3 install -r 'requirements-dev.txt'
```
source the `venv`
```commandline
source ./venv activate
```
deactivating the `venv`
```commandline
deactivate
```

### running the test suite
add a `parameters.json` file to the `/tests` directory with the following content:
```json
{
  "form_template_name": "unittest",
  "form_template_field_name": "test_field",
  "form_template_id": "f8fd0067-7a1f-e911-8b96-0800276652db"
}
```
a form template must be created named `unittest`, and must have a text box form field
named `test_field`. the `form_template_id` will be set to the `form_template_id` (GUID)
after form template creation in your VV environment.<br><br>
NOTE: this is just a work around until an API update happens for form template creation.<br><br>
add a `credentials.json` file to the `/tests` directory with the following content:
```json
{
  "url": "localhost/visualvault4_1_13",
  "customer_alias": "test_customer",
  "database_alias": "test_database",
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "email_address": "myemail@mydomain.com"
}
```
these `credentials` will be used to run the `VVRestTestSuite` against the
`VisualVault` environment in the `url` field.<br><br>
NOTE: tests should only be ran against a local or test instance of `VisualVault`
(not a production environment). <br><br>
Now that the files are configured for the `VVRestTestSuite`, run the following cmd:
```commandline
python3 -m unittest tests/vvrest_test_suite.py
```
running the `VVRestTestSuite` with `coverage` run the following cmd:
```commandline
coverage run --source vvrest -m unittest tests/vvrest_test_suite.py ; echo ; coverage report -m
```
running a specific `class` of tests in the test suite:
```commandline
python3 -m unittest tests.document_service_test.DocumentServiceTest
```
running a specific `test`:
```commandline
python3 -m unittest tests.document_service_test.DocumentServiceTest.test_get_documents
```

## contributing workflow
check out a feature branch based off of the latest in `develop`:
```commandline
git checkout develop
git pull
git checkout -b feature/my-cool-new-feature
```
commit/push all your `work` in the `feature branch` (do not commit to `develop` or `master` directly). 
submit a PR (Pull Request) in the GitHub UI setting the target branch to `develop`, and await feedback.
you will need to override the target base branch to `develop` since the default branch is `master`.
since this is an open source project the default branch will remain `master` 
(so people who clone the repo only get stable releases), but internally we can still use `gitflow`.
a repo maintainer will provide feedback, and handle merging the `feature branch` into `develop`. 
the `develop` branch is where all the work gets placed and staged for `releases`. 
the `master` branch is only updated alongside `releases` (stays even with latest release). 
NOTE: for users `forking` follow this same process in your `forked` repository.
