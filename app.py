# /usr/bin/env python
# -*- coding:utf-8 -*-

# file:app.py
# author:Ring
# datetime:2026/1/3 23:36
# software: PyCharm

"""
this is function  description 
"""
# import module your need
from flask import Flask
from models.todo_model import db
from controllers.todo_controller import todo_bp
from config.db_config import DB_CONFIG

# 初始化Flask应用
app = Flask(__name__, template_folder='views/templates')

# 配置SQLAlchemy（连接MySQL）
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/{DB_CONFIG['database']}?charset={DB_CONFIG['charset']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭不必要的警告

# 初始化数据库
db.init_app(app)

# 注册蓝图（路由）
app.register_blueprint(todo_bp)

# 创建数据库表（首次运行时执行）
with app.app_context():
    db.create_all()  # 自动根据模型创建表（若表不存在）

# 启动服务
if __name__ == '__main__':
    app.run(debug=True)