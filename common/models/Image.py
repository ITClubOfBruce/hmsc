# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    file_key = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='???')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
