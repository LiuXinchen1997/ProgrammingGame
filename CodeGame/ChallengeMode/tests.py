"""
tests.
"""

# Create your tests here.

from django.test import Client,TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import authenticate
import json

class ChallengeTest(TestCase):

    def setUp(self):
        self.user1 = {'username': 'liuxinchen', 'tel_number': '18755194465', 'password': 'e10adc3949ba59abbe56e057f20f883e'}
        self.c = Client()

    def test_getLevelByUsername(self):
        response = self.c.get('/ChallengeMode/getLevelByUsername', {'username': self.user1['username']})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['level'], self.user1['level'])

    def test_getAllLevels(self):
        response = self.c.get('/ChallengeMode/getAllLevels')
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_getChallengeMapContent(self):
        response = self.c.get('/ChallengeMode/getChallengeMapContent', {'level': 1})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['success'], True)

    def test_updateLevelOfUsername(self):
        response = self.c.get('/ChallengeMode/updateLevelOfUsername', {'username': self.user1['username'], level: 1})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])
