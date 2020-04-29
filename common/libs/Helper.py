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


# 根据数据库中的某个字段（id），查询出一个dict结果
def getDictFilterField(db_model,select_filed,key_filed,id_list):
    ret = {}
    query = db_model.query
    if id_list and len(id_list) > 0:
        query = query.filter(select_filed.in_(id_list))
    list = query.all()
    if not list:
        return ret
    for item in list:
        if not hasattr(item,key_filed):
            break
        if getattr(item,key_filed) not in ret:
            ret[getattr(item,key_filed)] = []

        ret[getattr(item,key_filed)].append(item)

    return ret 

def selectFilterObj(obj,field):
    ret = []
    for item in obj:
        if not hasattr(item,field):
            break
        if getattr(item,field) in ret:
            continue
        ret.append(getattr(item,field))
    return ret





