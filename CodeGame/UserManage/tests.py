"""
tests.
"""

# Create your tests here.

from django.test import Client,TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import authenticate
import json

class UserTest(TestCase):

    def setUp(self):
        self.user1 = {'username': 'liuxinchen', 'tel_number': '18755194465', 'password': 'e10adc3949ba59abbe56e057f20f883e'}
        self.c = Client()

    def test_UserEntryModels(self):
        self.assertEqual(self.user1['username'], 'liuxinchen')
        self.assertEqual(self.user1['password'], 'e10adc3949ba59abbe56e057f20f883e')
        self.assertEqual(self.user1['tel_number'], '18755194465')

    def testGetDemo(self):
        response = self.c.get('/UserManage/getDemo')
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['username'], 'aaa')
        self.assertEqual(res['password'], 'aaa')
        self.assertEqual(res['tel'], '13685620590')

    def testGetDemo(self):
        response = self.c.post('/UserManage/postDemo', {'username': self.user1['username']})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['username'], self.user1['username'])
        self.assertEqual(res['password'], self.user1['password'])
        self.assertEqual(res['tel'], self.user1['tel'])

    def testSendMessage(self):
        response = self.c.post('/UserManage/sendMessage', {'tel_number': '18755194465'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])
        self.assertEqual(res['verifyCode'], 0)

    def testTelNumExists(self):
        response = self.c.post('/UserManage/telNumExists', {'tel_number': '18755194465'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['exists'])

    def testRegister(self):
        response = self.c.post('/UserManage/register', {
            'username': 'ddd',
            'password': '123456',
            'gender': 1,
            'age': 20,
            'email': 'ddd@126.com',
            'fullname': 'Tom' })
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])

    def testMember(self):
        response = self.c.post('/UserManage/member', {'tel_number': '18755194465'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])
        self.assertEqual(res['verifyCode'], 0)

    def testUpdatePsw(self):
        response = self.c.post('/UserManage/UpdatePsd', {'userName': 'liuxinchen', 'password': '123456'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])

    def testUpdatePsdByTelNum(self):
        response = self.c.post('/UserManage/updatePsdByTelNum', {'telNumber': '18755194465', 'password': '123456'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])

    def testGetByUsername(self):
        response = self.c.post('/UserManage/getByUsername', {'username': 'liuxinchen'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])

    def testModifyInfo(self):
        response = self.c.post('/UserManage/modifyInfo', {
            'username': 'liuxinchen',
            'fullname': 'aaa',
            'email': 'liuxinchen1997@163.com',
            'gender': 'male'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])

    def testCheckPassword(self):
        response = self.c.post('/UserManage/checkPassword', {'username': 'liuxinchen', 'oldPassword': '123456'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['success'])

    def testGetUsernameByTel(self):
        response = self.c.post('/UserManage/getUsernameByTel', {'telnumber': '18755194465'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertEqual(res['username'], 'liuxinchen')

    def testMemberByUsername(self):
        response = self.c.post('/UserManage/getMemberByUsername', {'username': 'liuxinchen'})
        self.assertEqual(response.status_code, 200)
        res = json.loads(str(response.data, encoding='utf-8'))
        self.assertTrue(res['isMember'])
        self.assertEqual(res['priority'], 1)
