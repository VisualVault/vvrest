# *vvrest* release changelog

## v1.3.1
- `Token.token_expiration` is now timezone aware (UTC).
- update `AuthServiceTest` unittests.
- add `pytz` to package dependencies.

## v1.3.0
- user impersonation feature.
- add optional parameter `user_web_token` to `Vault`. if passed in, this
optional parameter will be used to authenticate on behalf of the user
that the `user_web_token` belongs to (user impersonation). if not passed in, 
then vv will authenticate on behalf of the user that the `client_id` and 
`client_secret` belong to.
- enhance `UserService` unittest with user impersonation.

## v1.2.1
- fix issue where user creation was failing in
`SiteService.create_site_user`, and `UserService.create_user`.
- additional `SiteService` and `UserService` unittests.
- add `setup_test_suite` to allow `VVRestTestSuite` to be ran against
any VisualVault environment.
- add `settings.py` to `tests`.
- add additional test utilities to `tests/utilities.py`.
- refactor all unittests to get test parameters from `parameters.json`.
- unittest `coverage` increase.
- add `CONTRIBUTING.md`.

## v1.2.0
- add `unittest` coverage for `FormService`.
- move `FormService.get_form_instances_search` functionality to `FormService.get_form_instances`.
- remove `FormService.get_form_instances_search`.
- add additional optional parameter `query` to `FormService.get_form_instances`.

## v1.1.0
- update dependencies for `PyPI` packaging so `README` can be rendered
properly as project description in `markdown`.
- the following `services` were added/removed because a `REST` client should
return a `FileStream` instead of downloading files. `IMO` it should be up to the 
subscriber of the `API` to do with the `FileStream` as they wish.
- services added:
    - `FormService.get_form_instance_pdf_file_stream`
    - `FileService.get_file_stream`
    - `FileService.get_file_stream_by_search`
- services removed:
    - `FormService.form_instance_pdf_download`
    - `FileService.file_download`
    - `FileService.file_download_by_search`
- added/removed `unittests`
- fix white space / tab issue (PEP8) on `FormService`
- update `README` with getting started `documentation`

## v1.0.0
- `PyPI` packaging
- `PEP8` code refactoring
- `unittest` coverage
- supports `python3`

## v1.0.0b1
- supports `python2`
- not a `PyPI` package
- supports the following general endpoints: `emails`, `documents`, `files`, 
`folders`, `forminstance`, `formtemplates`, `groups`, `indexfields`, 
`sites`, and `users`.
