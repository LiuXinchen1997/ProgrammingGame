"""
tests.
"""

# Create your tests here.

"""
tests.
"""

# Create your tests here.

from django.test import Client,TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import authenticate
import json

class FreeTest(TestCase):

    def setUp(self):
        self.user1 = {'username': 'liuxinchen', 'tel_number': '18755194465', 'password': 'e10adc3949ba59abbe56e057f20f883e'}
        self.c = Client()

    def test_getAllCreatedMapByUsername(self):
        response = self.c.get('/FreeMode/getAllCreatedMapByUsername', {'username': self.user1['username']})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_getAllReleasedMapByUsername(self):
        response = self.c.get('/FreeMode/getAllReleasedMapByUsername', {'username': self.user1['username']})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_getAllCollectedMapByUsername(self):
        response = self.c.get('/FreeMode/getAllCollectedMapByUsername', {'username': self.user1['username']})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_getAllReleasedMap(self):
        response = self.c.get('/FreeMode/getAllReleasedMap')
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_deleteMapById(self):
        response = self.c.get('/FreeMode/deleteMapById', {'map_id': 17})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_setLikeById(self):
        response = self.c.get('/FreeMode/setLikeById', {'username': self.user1['username'], 'map_id': 18})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_cancelLikeById(self):
        response = self.c.get('/FreeMode/cancelLikeById', {'username': self.user1['username'], 'map_id': 18})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_setCollectById(self):
        response = self.c.get('/FreeMode/setCollectById', {'username': self.user1['username'], 'map_id': 18})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_cancelCollectById(self):
        response = self.c.get('/FreeMode/cancelCollectById', {'username': self.user1['username'], 'map_id': 18})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_uploadFreeMapById(self):
        response = self.c.get('/FreeMode/uploadFreeMapById', {'map_id': 22})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)
