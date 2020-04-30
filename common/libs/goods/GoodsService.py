# -*- coding: utf-8 -*-
from application import app,db
from common.models.goods.Goods import Goods
from common.libs.Helper import getCurrentDate
class GoodsService():

    @staticmethod
    def setStockChangeLog( goods_id = 0,quantity = 0,note = '' ):

        if goods_id < 1:
            return False

        goods_info = Goods.query.filter_by( id = goods_id ).first()
        if not goods_info:
            return False

        model_stock_change = GoodsStockChangeLog()
        model_stock_change.goods_id = goods_id
        model_stock_change.unit = quantity
        model_stock_change.total_stock = goods_info.stock
        model_stock_change.note = note
        model_stock_change.created_time = getCurrentDate()
        db.session.add(model_stock_change)
        db.session.commit()
        return True


