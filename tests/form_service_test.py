import unittest
from .utilities import get_vault_object, generate_random_uuid
from vvrest.services.form_service import FormService


class FormServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        cls.form_template_id = 'ab34fcb3-870b-e911-a996-b95137116d54'
        cls.form_template_name = 'test_template'
        cls.form_instance_id = '328c018e-8a0b-e911-a9d0-f1f3158acf97'
        cls.form_instance_name = 'test_tem-000001'
        cls.form_template_field_name = 'test_field'
        cls.form_instance_field_value = 'test_field value'
        cls.document_revision_id = '8fefa9b6-56fa-e811-a995-a3d452a1c2f6'
        cls.document_id = '810013e6-50fa-e811-a9cf-8b72d90dd505'

    def test_get_form_templates(self):
        """
        tests FormService.get_form_templates
        """
        form_service = FormService(self.vault)
        resp = form_service.get_form_templates()

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        for form_template in resp['data']:
            self.assertEqual(form_template['dataType'], 'FormTemplate')

        resp = form_service.get_form_templates("name='" + self.form_template_name + "'")
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['dataType'], 'FormTemplate')
        self.assertEqual(resp['data'][0]['id'], self.form_template_id)
        self.assertEqual(resp['data'][0]['name'], self.form_template_name)

    def test_get_form_template(self):
        """
        tests FormService.get_form_template
        """
        form_service = FormService(self.vault)
        resp = form_service.get_form_template(self.form_template_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['dataType'], 'FormTemplate')
        self.assertEqual(resp['data'][0]['id'], self.form_template_id)
        self.assertEqual(resp['data'][0]['name'], self.form_template_name)

    def test_get_form_instance(self):
        """
        tests FormService.get_form_instance
        """
        form_service = FormService(self.vault)
        resp = form_service.get_form_instance(self.form_template_id, self.form_instance_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['dataType'], 'FormInstance')
        self.assertEqual(resp['data'][0]['revisionId'], self.form_instance_id)
        self.assertEqual(resp['data'][0]['instanceName'], self.form_instance_name)

    def test_get_form_instance_pdf_file_stream(self):
        """
        tests FormService.get_form_instance_pdf_file_stream
        example write stream to file:
        with open('tests/docs/test.pdf', 'wb') as form_pdf:
            form_pdf.write(stream.raw.read())
        """
        form_service = FormService(self.vault)
        stream = form_service.get_form_instance_pdf_file_stream(self.form_template_id, self.form_instance_id)

        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'text/html')

    def test_get_form_template_fields(self):
        """
        tests FormService.get_form_template_fields
        """
        form_service = FormService(self.vault)
        resp = form_service.get_form_template_fields(self.form_template_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertIn('fields', resp['data'])
        self.assertIn('baseFields', resp['data'])
        self.assertIn(self.form_template_field_name, resp['data']['fields'])

    def test_get_form_instances(self):
        """
        tests FormService.get_form_instances
        """
        form_service = FormService(self.vault)
        resp = form_service.get_form_instances(self.form_template_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        for form_instance in resp['data']:
            self.assertEqual(form_instance['dataType'], 'FormInstance')

        resp = form_service.get_form_instances(self.form_template_id, query="instanceName='" + self.form_instance_name + "'")

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        form_instance = resp['data'][0]
        self.assertEqual(form_instance['dataType'], 'FormInstance')
        self.assertEqual(form_instance['instanceName'], self.form_instance_name)

        resp = form_service.get_form_instances(self.form_template_id, query_string='fields=' + self.form_template_field_name)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        for form_instance in resp['data']:
            self.assertEqual(form_instance['dataType'], 'FormInstance')
            self.assertIn(self.form_template_field_name, form_instance)

        resp = form_service.get_form_instances(self.form_template_id,
                                               query="instanceName='" + self.form_instance_name + "'",
                                               query_string='fields=' + self.form_template_field_name)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        form_instance = resp['data'][0]
        self.assertEqual(form_instance['dataType'], 'FormInstance')
        self.assertEqual(form_instance['instanceName'], self.form_instance_name)
        self.assertIn(self.form_template_field_name, form_instance)
        self.assertEqual(form_instance[self.form_template_field_name], self.form_instance_field_value)

    def test_create_form_instance(self):
        """
        tests FormService.create_form_instance
        """
        form_service = FormService(self.vault)

        expected_field_value = generate_random_uuid()
        payload = dict(test_field=expected_field_value)

        resp = form_service.create_form_instance(self.form_template_id, payload)
        self.assertEqual(resp['meta']['status'], 201)
        self.assertEqual(resp['data']['dataType'], 'FormInstance')
        instance_id = resp['data']['revisionId']
        instance_name = resp['data']['instanceName']

        resp = form_service.get_form_instance(self.form_template_id, instance_id, query_string='fields=' + self.form_template_field_name)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        form_instance = resp['data'][0]
        self.assertEqual(form_instance['dataType'], 'FormInstance')
        self.assertEqual(form_instance['instanceName'], instance_name)
        self.assertIn(self.form_template_field_name, form_instance)
        self.assertEqual(form_instance[self.form_template_field_name], expected_field_value)

        expected_field_value = generate_random_uuid()
        payload = dict(test_field=expected_field_value)

        resp = form_service.create_form_instance_revision(self.form_template_id, instance_id, payload)
        self.assertEqual(resp['meta']['status'], 201)
        self.assertEqual(resp['data']['dataType'], 'FormInstance')
        instance_id = resp['data']['revisionId']
        instance_name = resp['data']['instanceName']

        resp = form_service.get_form_instance(self.form_template_id, instance_id, query_string='fields=' + self.form_template_field_name)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        form_instance = resp['data'][0]
        self.assertEqual(form_instance['dataType'], 'FormInstance')
        self.assertEqual(form_instance['instanceName'], instance_name)
        self.assertIn(self.form_template_field_name, form_instance)
        self.assertEqual(form_instance[self.form_template_field_name], expected_field_value)

    def test_relate_form(self):
        """
        tests the following FormService methods:
        relate_form, get_related_forms, unrelate_form
        """
        form_service = FormService(self.vault)
        payload = dict(test_field=generate_random_uuid())

        resp = form_service.create_form_instance(self.form_template_id, payload)
        self.assertEqual(resp['meta']['status'], 201)
        self.assertEqual(resp['data']['dataType'], 'FormInstance')
        instance_id2 = resp['data']['revisionId']

        resp = form_service.relate_form(self.form_instance_id, instance_id2)
        self.assertEqual(resp['meta']['status'], 200)

        resp = form_service.get_related_forms(self.form_instance_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['dataType'], 'FormInstance')
        self.assertEqual(resp['data'][0]['revisionId'], instance_id2)

        resp = form_service.unrelate_form(self.form_instance_id, instance_id2)
        self.assertEqual(resp['meta']['status'], 200)

        resp = form_service.get_related_forms(self.form_instance_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 0)

    def test_relate_document(self):
        """
        tests the following FormService methods:
        relate_document, get_related_documents, and unrelate_document
        """
        # TODO: report return list of object instead of object on FormInstance, and FormTemplate endpoints
        # TODO: report 404 if relationship already exists
        form_service = FormService(self.vault)

        resp = form_service.relate_document(self.form_instance_id, self.document_revision_id)
        self.assertEqual(resp['meta']['status'], 200)

        resp = form_service.get_related_documents(self.form_instance_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['dataType'], 'Document')
        self.assertEqual(resp['data'][0]['documentId'], self.document_id)

        resp = form_service.unrelate_document(self.form_instance_id, self.document_revision_id)
        self.assertEqual(resp['meta']['status'], 200)

        resp = form_service.get_related_documents(self.form_instance_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 0)
