# /usr/bin/env python
# -*- coding:utf-8 -*-

# file:todo_model.py
# author:Ring
# datetime:2026/1/3 23:33
# software: PyCharm

"""
this is function  description 
"""
# import module your need
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 初始化SQLAlchemy
db = SQLAlchemy()

class TodoModel(db.Model):
    __tablename__ = 'todolist'  # 对应数据库表名

    AutoID = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='事项ID')
    Title = db.Column(db.String(50), comment='事项名称')
    Status = db.Column(db.Integer, default=0, comment='状态（0:未完成 1:已完成）')
    IsDelete = db.Column(db.Integer, default=0, comment='是否删除')
    CreateTime = db.Column(db.DateTime, default=datetime.now, comment='添加时间')

    # 将模型转换为字典（用于前端渲染）
    def to_dict(self):
        return {
            "AutoID": self.AutoID,
            "Title": self.Title,
            "Status": self.Status,
            "CreateTime": self.CreateTime.strftime("%Y-%m-%d %H:%M:%S")
        }