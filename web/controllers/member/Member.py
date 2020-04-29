from flask import Blueprint,request,redirect,jsonify
from common.libs.Helper import ops_render


router_member = Blueprint("member_page",__name__)

@router_member.route("/index")
def index():
    return ops_render("member/index.html")
