from flask import g,render_template

import datetime


def ops_render(template,context={}):
    if 'current_user' in g:
        context["current_user"] = g.current_user
    return render_template(template,**context)

# 获取当前时间，并格式化
def getCurrentDate(format = "%Y-%m-%d %H:%M:%S" ):
    return datetime.datetime.now()

# 自定义分页
def iPagination(params):
    import math
    ret = {
        "is_prev":True,
        "is_next":True,
        "from":1,
        "end":0,
        "current":0,
        "total_pages":0,
        "page_size":0,
        "total":0,
        "url":params['url']
    }

    total = int(params['total'])
    page_size = int( params['page_size'] )
    page = int( params['page'] )
    total_pages = int( math.ceil(total/page_size))

    if page <= 1:
        ret['is_prev'] = False
    if page >= total_pages:
        ret['is_next'] = False
    
    ret['total'] = total
    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['end'] = total_pages

    # 生成器
    ret['range'] = range( ret['from'],ret['end'] + 1 )

    return ret

    







