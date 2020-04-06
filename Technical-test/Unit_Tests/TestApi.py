
import os
import unittest
import json
import urllib.request
from api import app
from flask import json
 
 
class BasicTests(unittest.TestCase):
 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/dataset"
        self.app = app.test_client()    
        self.assertEqual(app.debug, False)
    
    def tearDown(self):
        pass
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_result(self):
        results = self.app.get('/items')
        data=json.loads(results.get_data(as_text=True))

        self.assertEqual(results.status, '200 OK')
        self.assertEqual(data['count'], 5)
        #assert data['count'] == 5
 
 
if __name__ == "__main__":
    unittest.main()