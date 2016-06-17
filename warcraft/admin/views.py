from flask import render_template
from . import admin
from flask_login import login_required
from ..decorators import admin_required

@admin.route('/')
@admin.route('/index')
@login_required 
@admin_required
def index():
    return render_template('admin/index.html')