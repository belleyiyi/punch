'''
Created on Feb 20, 2014

@author: baobao
'''
import unittest

from punch import create_app,db
from punch.model import Parent,Child,District
from punch import ParentService,ChildService,DistrictService
 
class PunchAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.drop_all()
        self.app_context.pop()
 
class Test(PunchAppTestCase):
     
    def testParentChild(self):
        
        t_boy = ChildService().create(first_name='lu',
                      last_name='ln',
                      gender=1)
        t_girl = ChildService().create(first_name='lu',
                       last_name='nn',
                       gender=0)
        
        p = ParentService()
        
        district = DistrictService()
        
        district_record = district.create(name='putuo')
        record = p.create(first_name='lu',
                             last_name='qin',
                             qq='24062333',
                             phone_number='18615675426',
                             email='green@123.com',
                             gender=0,
                             child=[t_boy,t_girl],
                             district = district_record,
                             )
        
        
        print record.child[0].parent[0].first_name
        
        print t_boy.parent[0].first_name
        
        print record.district.name
        
        for item in p.all():
            print item.first_name


        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
