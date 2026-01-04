# /usr/bin/env python
# -*- coding:utf-8 -*-

# file:todo_controller.py
# author:Ring
# datetime:2026/1/3 23:36
# software: PyCharm

"""
this is function  description 
"""
# import module your need
from flask import Blueprint, render_template, request, jsonify
from models.todo_model import db, TodoModel

# 创建蓝图（路由模块）
todo_bp = Blueprint('todo', __name__)

# 首页：展示Todo列表
@todo_bp.route('/')
def index():
    # 查询未删除的Todo
    todos = TodoModel.query.filter_by(IsDelete=0).all()
    # 统计数据
    total = len(todos)
    done_count = len([t for t in todos if t.Status == 1])
    active_count = total - done_count
    return render_template(
        'index.html',
        todos=[t.to_dict() for t in todos],
        total=total,
        doneCount=done_count,
        activeCount=active_count
    )

# 添加Todo
@todo_bp.route('/add', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = TodoModel(Title=data.get('Title'))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"code": 200, "msg": "添加成功"})

# 更新状态（Done/Undo）
@todo_bp.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    todo = TodoModel.query.get(data.get('AutoID'))
    if todo:
        todo.Status = data.get('Status')
        db.session.commit()
        return jsonify({"code": 200, "msg": "状态更新成功"})
    return jsonify({"code": 404, "msg": "事项不存在"})

# 编辑Todo
@todo_bp.route('/edit', methods=['POST'])
def edit_todo():
    data = request.get_json()
    todo = TodoModel.query.get(data.get('AutoID'))
    if todo:
        todo.Title = data.get('Title')
        db.session.commit()
        return jsonify({"code": 200, "msg": "编辑成功"})
    return jsonify({"code": 404, "msg": "事项不存在"})

# 删除Todo（逻辑删除）
@todo_bp.route('/delete', methods=['POST'])
def delete_todo():
    data = request.get_json()
    todo = TodoModel.query.get(data.get('AutoID'))
    if todo:
        todo.IsDelete = 1
        db.session.commit()
        return jsonify({"code": 200, "msg": "删除成功"})
    return jsonify({"code": 404, "msg": "事项不存在"})