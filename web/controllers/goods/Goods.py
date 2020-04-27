from flask import Blueprint
from application import app
from common.libs.Helper import ops_render

router_goods = Blueprint("goods_page",__name__)

@router_goods.route('/index')
def index():
    resp_data = {}
    return ops_render('/goods/index.html')
@router_goods.route( "/info" )
def info():
    resp_data = {}
    return ops_render( "goods/info.html",resp_data )
@router_goods.route( "/set" ,methods = [ 'GET','POST'] )
def set():
    resp_data = {}
    return ops_render( "goods/set.html",resp_data )
@router_goods.route( "/cat" )
def cat():
    resp_data = {}
    return ops_render( "goods/cat.html",resp_data )

@router_goods.route( "/cat-set",methods = [ "GET","POST" ] )
def catSet():
    resp_data = {}
    return ops_render( "goods/cat_set.html",resp_data )