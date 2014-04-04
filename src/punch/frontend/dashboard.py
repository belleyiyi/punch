'''
Created on Feb 24, 2014

@author: green
'''
from flask import Blueprint, render_template,request,flash
from ..forms import RegistrationForm
from ..service import ParentService,ChildService,DistrictService



dashboard = Blueprint('dashboard', __name__,template_folder='templates')



@dashboard.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
#     print form.validate()
    if request.method == 'POST':
#         district_record = DistrictService().create(name='putuo')
        
        flash('Thanks for registering')
        return render_template('registration.html', form=form,childform=[[]])
    return render_template('registration.html', form=form,childform=[[]])

@dashboard.route('/registerlist',methods=['GET','POST'])
def registerlist():
    pass

@dashboard.route('/admin', methods=['GET', 'POST'])
def admin():
    print 'printing' ,request.form
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
#         return redirect(url_for('login'))
    return render_template('frame.html', left='/left',right='/right')

@dashboard.route('/left', methods=['GET', 'POST'])
def left():
    return render_template('left.html')

@dashboard.route('/right', methods=['GET', 'POST'])
def right():
    return render_template('right.html')
