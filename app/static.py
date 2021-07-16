# -*- coding: utf-8 -*-
from flask import Blueprint

app = Blueprint('static', __name__, static_url_path='', static_folder='../static')