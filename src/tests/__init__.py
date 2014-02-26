from unittest import TestCase

from punch import create_app,db

class PunchAppTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.drop_all()
        self.app_context.pop()