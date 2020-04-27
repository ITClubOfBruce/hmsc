from flask import g,render_template

import datetime


def ops_render(template,context={}):
    if 'current_user' in g:
        context["current_user"] = g.current_user
    return render_template(template,**context)

# 获取当前时间，并格式化
def getCurrentDate(format = "%Y-%m-%d %H:%M:%S" ):
    return datetime.datetime.now()