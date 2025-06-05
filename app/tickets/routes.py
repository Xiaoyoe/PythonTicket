from flask import Blueprint, jsonify, request, Response
from werkzeug.exceptions import BadRequest
from app.tickets.models import Ticket
from app.tickets.schemas import ticket_schema, tickets_schema
import os

# 创建 tickets 蓝图
tickets_bp = Blueprint('tickets', __name__)

# 图片存储目录（根据实际情况修改）
IMAGE_DIR = 'static/images'

# 查找与 image_res_id 匹配的图片文件并返回完整文件名
def find_image_file(image_res_id):
    for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
        filename = f"{image_res_id}{ext}"
        file_path = os.path.join(IMAGE_DIR, filename)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return filename
    return None

# 获取所有票务信息，包含完整的图片 URL
@tickets_bp.route('/', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    result = []

    for ticket in tickets:
        # 获取票务的基本信息
        ticket_data = ticket_schema.dump(ticket)

        # 查找对应的图片文件
        image_filename = find_image_file(ticket.image_res_id)

        if image_filename:
            # 构建完整的图片 URL，包含文件名和后缀
            ticket_data['image_url'] = f"http://127.0.0.1:5000/tickets/images/{image_filename}"

        result.append(ticket_data)

    return jsonify(result), 200


# 根据类型获取票务
@tickets_bp.route('/<string:ticket_type>', methods=['GET'])
def get_tickets_by_type(ticket_type):
    # **核心修改**：将请求的小写类型转为数据库中的大写类型（如movie→MOVIE）
    db_type = ticket_type.upper()  # 转为大写，匹配数据库中的类型值

    # 检查类型是否存在（可根据实际业务扩展允许的类型）
    allowed_types = ['MOVIE', 'CONCERT', 'MUSIC', 'COMEDY']  # 对应数据库中的type值
    if db_type not in allowed_types:
        return jsonify({
            'status': 'error',
            'message': f'Invalid type. Allowed types: {allowed_types}'
        }), 400

    # 查询数据库（直接匹配type字段的大写值）
    tickets = Ticket.query.filter_by(type=db_type).all()

    result = []
    for ticket in tickets:
        data = ticket_schema.dump(ticket)
        image_filename = find_image_file(ticket.image_res_id)
        if image_filename:
            data['image_url'] = f"http://127.0.0.1:5000/tickets/images/{image_filename}"
        result.append(data)

    return jsonify(result), 200


# 根据 ID 获取单个票务信息
@tickets_bp.route('/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    # 查找对应的图片文件
    image_filename = find_image_file(ticket.image_res_id)

    if image_filename:
        # 构建完整的图片 URL，包含文件名和后缀
        ticket_data = ticket_schema.dump(ticket)
        ticket_data['image_url'] = f"http://127.0.0.1:5000/tickets/images/{image_filename}"
        return jsonify(ticket_data), 200

    # 如果找不到图片，返回原始数据
    return jsonify(ticket_schema.dump(ticket)), 200

# 图片流接口，返回图片的二进制数据
@tickets_bp.route('/images/<filename>', methods=['GET'])
def get_image_stream(filename):
    try:
        # 构建完整的图片路径
        image_path = os.path.join(IMAGE_DIR, filename)

        # 检查文件是否存在
        if not os.path.exists(image_path):
            return jsonify({'status': 'error', 'message': 'Image not found'}), 404

        # 检查是否是文件
        if not os.path.isfile(image_path):
            return jsonify({'status': 'error', 'message': 'Not a valid file'}), 400

        # 获取文件扩展名，用于设置 Content-Type
        ext = os.path.splitext(filename)[1].lower()

        # 根据文件扩展名设置 MIME 类型
        content_type = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.webp': 'image/webp'
        }.get(ext, 'application/octet-stream')

        # 以二进制模式读取文件并返回流式响应
        def generate():
            with open(image_path, 'rb') as f:
                while True:
                    chunk = f.read(4096)  # 每次读取 4KB
                    if not chunk:
                        break
                    yield chunk

        return Response(generate(), content_type=content_type)

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500