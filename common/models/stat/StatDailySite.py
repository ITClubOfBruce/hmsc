# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, Numeric
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db

class StatDailySite(db.Model):
    __tablename__ = 'stat_daily_site'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True, info='??')
    total_pay_money = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='??????')
    total_member_count = db.Column(db.Integer, nullable=False, info='????')
    total_new_member_count = db.Column(db.Integer, nullable=False, info='???????')
    total_order_count = db.Column(db.Integer, nullable=False, info='?????')
    total_shared_count = db.Column(db.Integer, nullable=False, info='????')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='??????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
