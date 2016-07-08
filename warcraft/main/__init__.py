from flask import Blueprint

main = Blueprint('main', __name__) 

from . import views, errors
from ..models import FPermission


@main.app_context_processor
def inject_permissions():
    return dict(FPermission=FPermission)