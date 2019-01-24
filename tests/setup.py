import os
import json
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json, get_random_string
from vvrest.services.document_service import DocumentService
from vvrest.services.folder_service import FolderService
from vvrest.services.form_service import FormService
from vvrest.services.index_field_service import IndexFieldService
from vvrest.services.site_service import SiteService
from vvrest.services.group_service import GroupService
from vvrest.services.user_service import UserService
from vvrest.services.file_service import FileService
from .settings import parameters_file, test_file_path


def setup_test_suite():
    """
    updates parameters.json for VVRestTestSuite
    """
    vault = get_vault_object()

    document_service = DocumentService(vault)
    folder_service = FolderService(vault)
    form_service = FormService(vault)
    index_field_service = IndexFieldService(vault)
    site_service = SiteService(vault)
    group_service = GroupService(vault)
    user_service = UserService(vault)
    file_service = FileService(vault)

    # create folder
    expected_folder_name = generate_random_uuid()
    expected_folder_description = expected_folder_name + ' description'
    resp = folder_service.new_folder(expected_folder_name, expected_folder_description, True)
    folder_id = resp['data']['id']
    folder_path = '/' + expected_folder_name
    query_string = "folderPath='" + folder_path + "'"

    # create sub folder
    expected_sub_folder_name = generate_random_uuid()
    expected_sub_folder_description = expected_sub_folder_name + ' description'
    resp = folder_service.new_sub_folder(folder_id, expected_sub_folder_name, expected_sub_folder_description, True)
    assert resp['meta']['status'] == 200
    sub_folder_id = resp['data']['id']
    sub_folder_path = folder_path + '/' + expected_sub_folder_name

    # create index field definition
    expected_label = get_random_string(10)
    expected_description = expected_label + ' description'
    resp = index_field_service.create_index_field(expected_label, expected_description, 1, True, 'DEFAULT')
    assert resp['meta']['status'] == 200
    index_field_id = resp['data']['id']
    index_field_name = expected_label

    # relate index field definition to folder
    resp = index_field_service.relate_index_field_to_folder(index_field_id, folder_id)
    assert resp['meta']['status'] == 200

    # create document
    resp = document_service.new_document(folder_id, 1, '_test_doc', '_test_doc description', '0', '_test.txt')
    assert resp['meta']['status'] == 200
    document_id = resp['data']['documentId']

    # create document revision (file upload)
    expected_revision = generate_random_uuid()
    resp = file_service.file_upload(document_id, 'unittest', expected_revision, 'unittest change reason',
                                    'Released', '', 'unittest.txt', test_file_path + '/test_file.txt')

    assert resp['meta']['status'] == 200

    # get document revision
    resp = document_service.get_document(document_id)
    assert resp['meta']['status'] == 200
    document_revision_id = resp['data']['id']

    # create site
    expected_site_name = generate_random_uuid()
    expected_site_description = expected_site_name + ' description'
    resp = site_service.create_site(expected_site_name, expected_site_description)
    assert resp['meta']['status'] == 200
    site_id = resp['data']['id']

    # create new group
    expected_group_name = generate_random_uuid()
    expected_group_description = expected_group_name + ' description'
    resp = group_service.create_group(expected_group_name, expected_group_description, site_id)
    assert resp['meta']['status'] == 200
    group_id = resp['data']['id']

    # create user
    user_id = generate_random_uuid()
    first_name = 'test'
    last_name = 'test'
    email = 'test@visualvault.com'
    password = 'TsT3!aB4@sY7'
    resp = user_service.create_user(site_id, user_id, first_name, last_name, email, password)
    assert resp['meta']['status'] == 200
    user_id = resp['data']['id']

    # add user to group
    resp = group_service.add_user_to_group(group_id, user_id)
    assert resp['meta']['status'] == 201

    # get form params TODO: remove with API update
    parameters_json = get_parameters_json()
    form_template_id = parameters_json['form_template_id']
    form_instance_field_name = parameters_json['form_template_field_name']
    form_template_name = parameters_json['form_template_name']

    # create form instance
    form_instance_field_value = generate_random_uuid()
    payload = {form_instance_field_name: form_instance_field_value}

    resp = form_service.create_form_instance(form_template_id, payload)
    assert resp['meta']['status'] == 201
    form_instance_id = resp['data']['revisionId']
    form_instance_name = resp['data']['instanceName']

    # setup test_parameters json
    if os.path.isfile(parameters_file):
        parameters = get_parameters_json()
        parameters['folder_path'] = folder_path
        parameters['query_string'] = query_string
        parameters['document_id'] = document_id
        parameters['document_revision_id'] = document_revision_id
        parameters['index_field_id'] = index_field_id
        parameters['index_field_name'] = index_field_name
        parameters['folder_id'] = folder_id
        parameters['folder_name'] = expected_folder_name
        parameters['sub_folder_id'] = sub_folder_id
        parameters['sub_folder_path'] = sub_folder_path
        parameters['site_id'] = site_id
        parameters['group_id'] = group_id
        parameters['user_id'] = user_id
        parameters['form_instance_name'] = form_instance_name
        parameters['form_instance_id'] = form_instance_id
        parameters['form_instance_field_value'] = form_instance_field_value
    else:
        parameters = dict(
            folder_path=folder_path,
            query_string=query_string,
            document_id=document_id,
            document_revision_id=document_revision_id,
            index_field_id=index_field_id,
            index_field_name=index_field_name,
            folder_id=folder_id,
            folder_name=expected_folder_name,
            sub_folder_id=sub_folder_id,
            sub_folder_path=sub_folder_path,
            site_id=site_id,
            group_id=group_id,
            user_id=user_id,
            form_instance_name=form_instance_name,
            form_instance_id=form_instance_id,
            form_instance_field_value=form_instance_field_value
        )

    with open(parameters_file, 'w+') as parameters_json:
        json.dump(parameters, parameters_json)  # write test_parameters to parameters.json
