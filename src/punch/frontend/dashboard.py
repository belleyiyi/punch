'''
Created on Feb 24, 2014

@author: green
'''
from flask import Blueprint, render_template,request,\
                    flash,redirect,url_for,session,abort

from ..forms import RegistrationForm
from ..service import ParentService,ChildService,DistrictService

dashboard = Blueprint('dashboard', __name__,template_folder='templates')

# @dashboard.before_request
# def csrf_protect():
#     if request.method == "POST":
#         token = session.pop('_csrf_token', None)
#         if not token or token != request.form.get('_csrf_token'):
#             abort(403)


@dashboard.route('/register', methods=['GET', 'POST'])
def register():
    district_record = DistrictService()
    form = RegistrationForm(request.form)
#     form.district.choices = [(str(d.id),str(d.name)) for d in DistrictService().all()]
#     print form.district
    print form.validate()
    print form.errors
    if form.validate_on_submit():
        
#         form.data.clear()
#         district_record = DistrictService()
#         for item in district_record.all():
#             print item.name
#         print form.validate
        
        flash('Thanks for registering')
        return render_template('registration.html', form=form)
#         return redirect(url_for('register'))
    return render_template('registration.html', form=form)

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
