'''
Created on Feb 24, 2014

@author: green
'''
from flask import Blueprint, render_template,request,flash
from ..forms import RegistrationForm


registration = Blueprint('register', __name__,template_folder='templates')



@registration.route('/register', methods=['GET', 'POST'])
def register():
    print 'printing' ,request.form
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
#         return redirect(url_for('login'))
    return render_template('registration.html', form=form,childform=[[]])