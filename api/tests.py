import unittest
from django.test import Client
import json


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get('/employee/')
        expected = json.loads('{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 0}, "objects": []}')
        actual = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected, actual)
        self.assertIsNotNone(actual['objects'])