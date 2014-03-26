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


@registration.route('/admin', methods=['GET', 'POST'])
def admin():
    print 'printing' ,request.form
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
#         return redirect(url_for('login'))
    return render_template('frame.html', left='/left',right='/right')

@registration.route('/left', methods=['GET', 'POST'])
def left():
    print 'printing' ,request.form
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
#         return redirect(url_for('login'))
    return render_template('left.html')

@registration.route('/right', methods=['GET', 'POST'])
def right():
    print 'printing' ,request.form
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
#         return redirect(url_for('login'))
    return render_template('right.html')