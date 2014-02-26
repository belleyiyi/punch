'''
Created on Feb 20, 2014

@author: baobao
'''
import unittest
# 
from tests import PunchAppTestCase
from punch.model import Parent,Child
from punch import ParentService,ChildService
 
 
class Test(PunchAppTestCase):
     
    def testParentChild(self):
        
        t_boy = ChildService().create(first_name='lu',
                      last_name='ln',
                      gender=1)
        t_girl = ChildService().create(first_name='lu',
                       last_name='nn',
                       gender=0)
        
        p = ParentService()
        record = p.create(first_name='lu',
                             last_name='qin',
                             qq='24062333',
                             phone_number='18615675426',
                             email='green@123.com',
                             password='password',
                             gender=0,
                             child=[t_boy,t_girl])
        
        
        print record.child[0].parent[0].first_name
        
        print t_boy.parent[0].first_name
        
        for item in p.all():
            print item.first_name


        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
