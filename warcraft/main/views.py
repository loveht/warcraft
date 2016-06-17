from datetime import datetime
from flask import render_template, current_app,session, redirect, url_for, request
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from flask_babel import Babel, gettext as _

from . import main

from .. import db, babel
from ..models import Permission, Role, User, Post, Comment
from ..decorators import admin_required, permission_required

@babel.localeselector
def get_locale():
    return 'zh' #request.accept_languages.best_match(current_app.config['LANGUAGES'].keys())

@main.route('/')
@main.route('/index')
def index():
    title = _("Title")
    return render_template('index.html', name=current_app.config['APP_NAME'], title = title)


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['WARCRAFT_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('user.html', user=user, posts=posts,
                           pagination=pagination)