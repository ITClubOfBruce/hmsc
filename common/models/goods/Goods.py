# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db


class Good(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='??id')
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='????')
    price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='????')
    main_image = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='????')
    summary = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue(), info='????')
    stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='???')
    tags = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='tag ????","??')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:???0???')
    month_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='???')
    total_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='???')
    view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?????')
    comment_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='????')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
