#coding:utf-8
"'auth的蓝本'"
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views