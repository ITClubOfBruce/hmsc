from flask import Blueprint

from common.libs.Helper import ops_render

router_account = Blueprint("account_page",__name__)

@router_account.route('/index',)
def index():
    return ops_render('account/index.html')

@router_account.route('/info',)
def info():
    return ops_render('account/info.html')

@router_account.route('/set',)
def set():
    return ops_render('account/set.html')