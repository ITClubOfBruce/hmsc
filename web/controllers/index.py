from application import app
from flask import Blueprint,render_template
from common.libs.Helper import ops_render
from common.models.stat.StatDailySite import StatDailySite

route_index = Blueprint("index_page",__name__)

@route_index.route('/')
def index():
    resp_data = {
        'data':{
            'finance':{
                'today':0,
                'month':0
            },
            'order':{
                'today':0,
                'month':0
            },
            'member':{
                'today_new':0,
                'month_new':0,
                'total':0
            },
            'shared':{
                'today':0,
                'month':0
            }
        }
    }

    # 日期格式化的问题
    # 更新数据的问题
    StatDailySite.query.all()
    return ops_render("index/index.html",resp_data)
   