from flask import Blueprint,request,jsonify,make_response,redirect,g

from application import app,db
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
    response = make_response(redirect(UrlManager.buildUrl("/user/login")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response

@router_user.route("/edit",methods=['GET','POST'])
def edit():
    if request.method == "GET":
        return ops_render("user/edit.html")
    # POST请求
    resp = {
        'code':200,
        'msg':'编辑成功',
        'data':{}
    }

    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    email = req['email'] if 'email' in req else ''
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入规范的nickname"
        return jsonify(resp)
    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入规范的email"
        return jsonify(resp)
    
    # 别忘了g
    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email

    db.session.add(user_info)
    db.session.commit()
    return jsonify(resp)
    

@router_user.route("/reset-pwd",methods=['GET','POST'])
def resetPwd():
    if request.method == "GET":
        return ops_render("user/reset_pwd.html")
    # POST请求
    resp = {
        'code':200,
        'msg':'重置密码成功',
        'data':{}
    }

    req = request.values
    old_password = req['old_password'] if 'old_password' in req else ''
    new_password = req['new_password'] if 'new_password' in req else ''

    if old_password is None or len(old_password) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的旧密码"
        return jsonify(resp)
    if new_password is None or len(new_password) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的新密码"
        return jsonify(resp)
    
    if old_password == new_password:
        resp['code'] = -1
        resp['msg'] = "新密码和旧密码不能相同"
        return jsonify(resp)
    
    user_info = g.current_user
    #演示账号的保护
    # if user_info.uid == 1:
    #     pass
    
    user_info.login_pwd = UserService.generatePwd(new_password,user_info.login_salt)

    db.session.add(user_info)
    db.session.commit()

    # 修改cookie中的旧用户信息
    response = make_response(json.dumps(resp))
    # Cookie中存入的信息是user_info.uid,user_info
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s@%s"%(UserService.generateAuthCode(user_info),user_info.uid),60*60*24*15)
    return response