'''
Created on Feb 24, 2014

@author: green
'''
from flask import Blueprint, render_template,request,flash
from ..forms import RegistrationForm



dashboard = Blueprint('dashboard', __name__,template_folder='templates')



@dashboard.route('/register', methods=['GET', 'POST'])
def register():
    print 'printing' ,request.form
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
#         return redirect(url_for('login'))
    return render_template('registration.html', form=form,childform=[[]])


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