# *vvrest* release changelog

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
