from flask import Blueprint,request,jsonify,redirect

from common.libs.Helper import ops_render,getCurrentDate,iPagination
from common.libs.UrlManager import UrlManager
from common.models.goods.Goods import Goods
from application import app,db

router_goods = Blueprint("goods_page",__name__)

@router_goods.route("/index")
def index():
    resp_data = {}
    query = Goods.query
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    if 'status' in req and int(req['status']) > -1:
        query = query.filter(Goods.status == int(req['status']))
    if 'mix_kw' in req:
        rule = or_( Goods.name.ilike("%{0}%".format(req['mix_kw'])), Goods.tags.ilike("%{0}%".format(req['mix_kw'])) )
        query = query.filter(rule)
    if 'cat_id' in req and int(req['cat)id']) > 0:
        query = query.filter(Goods.cat_id == int(req['cat_id']))
    params = {
        "total":query.count(),
        "page_size":2,
        "page":page,
        "url":request.full_path.replace("&p={}".format(page),"")
    }
    pages = iPagination(params)
    # 当前页数据开始位置  
    offset = (page-1) * 2
    # 当前页数据结束位置  
    limit = page * 2

    list = query.all()[offset:limit]

    resp_data['list'] = list
    resp_data['pages'] = pages
    return ops_render("goods/index.html",resp_data)


@router_goods.route("/info")
def info():
    resp_data = {}

    return ops_render("goods/info.html")

@router_goods.route("/set",methods=['GET','POST'])
def set():
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int(req.get('id',0))
        info = Goods.query.filter_by(id=id).first()
        if info and info.status != 1:
            return redirect(UrlManager.buildUrl("/goods/index"))
        resp_data['info'] = info
        return ops_render("goods/set.html",resp_data)
    # POST
    resp = {
        'code':200,
        'msg':"操作成功",
        'data':{}
    }
    req = request.values
    id = int(req['id']) if 'id' in req and req['id'] else 0
    cat_id = int(req['cat_id']) if 'cat_id' in req else 0
    name = req['name'] if 'name' in req else ''
    price = req['price'] if 'price' in req else ''
    main_image = req['main_image'] if 'main_image' in req else ''
    summary = req['summary'] if 'summary' in req else ''
    stock = int(req['stock']) if 'stock' in req else ''
    tags = req['tags'] if 'tags' in req else ''

    if cat_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择分类"
        return jsonify(resp)

    if name is None or len(name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的名称"
        return jsonify(resp)

    if not price or len(price) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的价格"
        return jsonify(resp)
    price = Decimal(price).quantize(Decimal('0.00'))
    if price < 0:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的价格"
        return jsonify(resp)
    
    if main_image is None or len(main_image) < 3:
        resp['code'] = -1
        resp['msg'] = "请上传封面"
        return jsonify(resp)

    if summary is None or len(summary) < 3:
        resp['code'] = -1
        resp['msg'] = "请输入商品描述，不少于10个字符"
        return jsonify(resp)
    
    if stock < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的库存量"
        return jsonify(resp)
    
    if tags is None or len(tags) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入标签，便于搜索"
        return jsonify(resp)

    goods_info = Goods.query.filter_by(uid=id).first()
    before_stock = 0
    if goods_info:
        model_goods = goods_info
        before_stock = model_goods.stock 
    else:
        model_goods = Goods()
        model_goods.status = 1
        # 插入格式化的时间
        model_goods.created_time = getCurrentDate()
    model_goods.cat_id = cat_id
    model_goods.name = name
    model_goods.price = price
    model_goods.main_image = main_image
    model_goods.summary = summary
    model_goods.stock = stock
    model_goods.tags = tags
    model_goods.updated_time = getCurrentDate()

    db.session.add(model_goods)
    db.session.commit()     
    return jsonify(resp)

@router_goods.route("/cat")
def cat():
    resp_data = {}

    return ops_render("goods/cat.html")



@router_goods.route("/cat_set")
def cat_set():
    resp_data = {}

    return ops_render("goods/cat_set.html")