'''
Created on Feb 20, 2014

@author: baobao
'''
from punch import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
