from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from app import db
from app.auth.models import User
from app.auth.schemas import user_schema

# 创建认证模块的蓝图，用于组织路由
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET'])
def hello_world():
    # 认证模块根路由，返回简单的提示信息
    return "这是认证接口"


@auth_bp.route('/register', methods=['POST'])
def register():
    # 用户注册接口
    # - 接收JSON格式数据：{username, email, password}
    # - 验证必填字段和唯一性约束
    # - 创建新用户并存储到数据库
    data = request.get_json()

    # 检查请求是否包含JSON数据
    if not data:
        raise BadRequest('No input data provided')

    # 从请求数据中提取用户信息
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # 验证必填字段
    if not username or not email or not password:
        raise BadRequest('Missing required fields')

    # 检查用户名是否已存在
    if User.query.filter_by(username=username).first():
        raise BadRequest('Username already exists')

    # 检查邮箱是否已存在
    if User.query.filter_by(email=email).first():
        raise BadRequest('Email already exists')

    # 创建新用户对象（密码以明文形式存储，注意安全风险）
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    # 返回创建成功的用户信息
    return jsonify({'success': True, 'message': '注册成功！', 'data': user_schema.dump(user)}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    # 用户登录接口
    # - 接收JSON格式数据：{username, password}
    # - 验证用户身份
    # - 返回登录成功消息
    data = request.get_json()

    # 检查请求是否包含JSON数据
    if not data:
        raise BadRequest('No input data provided')

    # 从请求数据中提取登录凭证
    username = data.get('username')
    password = data.get('password')

    # 验证必填字段
    if not username or not password:
        raise BadRequest('Missing required fields')

    # 查询用户信息
    user = User.query.filter_by(username=username).first()

    # 验证用户是否存在以及密码是否匹配（明文比较，注意安全风险）
    if not user or user.password != password:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 400

    # 返回登录成功消息
    return jsonify({'success': True, 'message': '登录成功！'}), 200


@auth_bp.route('/profile', methods=['GET'])
def get_profile():
    # 获取用户个人信息接口
    # - 通过查询参数接收user_id
    # - 返回对应用户的详细信息
    user_id = request.args.get('user_id')

    # 验证是否提供了用户ID
    if not user_id:
        raise BadRequest('Missing user ID')

    # 查询用户信息（若不存在则返回404错误）
    user = User.query.get_or_404(user_id)

    # 返回用户信息
    return jsonify(user_schema.dump(user)), 200


@auth_bp.route('/public', methods=['GET'])
def get_all_users():
    # 获取所有用户信息接口（公开接口，慎用）
    # - 返回系统中所有用户的基本信息列表
    users = User.query.all()
    user_list = [user.to_dict() for user in users]

    # 返回用户列表
    return jsonify({
        'status': 'success',
        'count': len(user_list),
        'data': user_list
    }), 200