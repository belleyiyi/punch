'''
Created on Feb 20, 2014

@author: baobao
'''
from punch import frontend

if __name__ == '__main__':
    app = frontend.create_app()
    app.run(debug=True)