from flask import Blueprint,jsonify
from app import db
from app.auth.models import User


# 创建测试蓝图，使用唯一的名称
test_bp = Blueprint('test', __name__)

@test_bp.route('/', methods=['GET'])
def hello_world():
    return "这是测试接口"


@test_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        # 查询所有用户
        users = User.query.all()

        # 构建响应数据
        user_list = []
        for user in users:
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phone': user.phone,
                'address': user.address,
                'is_admin': user.is_admin
            }
            user_list.append(user_data)

        return jsonify({
            'status': 'success',
            'count': len(user_list),
            'data': user_list
        }), 200

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500