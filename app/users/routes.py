from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from app import db
from app.auth.models import User
from .schemas import user_profile_schema

# 创建测试蓝图，使用唯一的名称
users_bp = Blueprint('users', __name__)


# 获取当前用户的个人资料
@users_bp.route('/profile', methods=['GET'])
def get_user_profile():
    user_id = request.args.get('user_id')
    if not user_id:
        raise BadRequest('Missing user ID')
    user = User.query.get_or_404(user_id)  # 查询用户
    return jsonify(user_profile_schema.dump(user)), 200  # 返回用户资料


# 更新当前用户的个人资料
@users_bp.route('/profile', methods=['PUT'])
def update_user_profile():
    data = request.get_json()  # 获取JSON格式的请求数据

    if not data:
        raise BadRequest('No input data provided')

    user_id = request.args.get('user_id')
    if not user_id:
        raise BadRequest('Missing user ID')
    user = User.query.get_or_404(user_id)  # 查询用户

    # 更新用户资料（只更新请求中提供的字段）
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'phone' in data:
        user.phone = data['phone']
    if 'address' in data:
        user.address = data['address']

    db.session.commit()  # 提交数据库变更
    return jsonify(user_profile_schema.dump(user)), 200  # 返回更新后的用户资料