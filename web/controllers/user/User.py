from flask import Blueprint,request,jsonify,make_response,redirect,g

from application import app
from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
from common.libs.Helper import ops_render

import json

router_user = Blueprint('user_page',__name__)

@router_user.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if g.current_user:
            return redirect(UrlManager.buildUrl("/"))
        return ops_render("user/login.html")
        
    # POST请求
    resp = {
        'code':200,
        'msg':'登录成功',
        'data':{}
    }
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户名"
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码"
        return jsonify(resp)
    # 从数据库中取出user
    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "用户不存在"
        return jsonify(resp)
    # 判断密码
    if user_info.login_pwd != UserService.generatePwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "密码输入错误"
        return jsonify(resp)
    
    # 判断用户状态
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = "用户已经被禁用，请联系管理员处理"
        return jsonify(resp)
    
    
    response = make_response(json.dumps({'code':200,'msg':'登录成功~~~'}))
    # Cookie中存入的信息是user_info.uid,user_info
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s@%s"%(UserService.generateAuthCode(user_info),user_info.uid),60*60*24*15)
    return response
    

@router_user.route("/logout")
def logout():
    return "登出"

@router_user.route("/edit")
def edit():
    return ops_render("user/edit.html")

@router_user.route("/reset-pwd")
def resetPwd():
    return ops_render("user/reset_pwd.html")