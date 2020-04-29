# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db

class MemberComment(db.Model):
    __tablename__ = 'member_comments'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='??id')
    goods_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='??id')
    pay_order_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='??id')
    score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='??')
    content = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
