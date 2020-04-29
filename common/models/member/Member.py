# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db



class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='????')
    mobile = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='??????')
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:? 2:? 0:????')
    avatar = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='????')
    salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='?????????')
    reg_ip = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??ip')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:?? 0:??')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
