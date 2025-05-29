from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from app.stuffs.models import Stuff
from app.stuffs.schemas import stuff_schema, stuffs_schema

# 创建 stuffs 蓝图
stuffs_bp = Blueprint('stuffs', __name__)

@stuffs_bp.route('/', methods=['GET'])
def get_stuffs():
    """获取所有商品信息"""
    stuffs = Stuff.query.all()
    return jsonify(stuffs_schema.dump(stuffs)), 200

@stuffs_bp.route('/<int:stuff_id>', methods=['GET'])
def get_stuff(stuff_id):
    """根据ID获取单个商品信息"""
    stuff = Stuff.query.get_or_404(stuff_id)
    return jsonify(stuff_schema.dump(stuff)), 200