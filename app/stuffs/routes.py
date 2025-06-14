from flask import Blueprint, jsonify, request, Response
from werkzeug.exceptions import BadRequest
from app.stuffs.models import Stuff
from app.stuffs.schemas import stuff_schema, stuffs_schema
import os

# 创建 stuffs 蓝图
stuffs_bp = Blueprint('stuffs', __name__)

# 图片存储目录（根据实际情况修改）
IMAGE_DIR = 'static/images'


def find_image_file(image_res_id):
    """查找与image_res_id匹配的图片文件并返回完整文件名"""
    for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
        filename = f"{image_res_id}{ext}"
        file_path = os.path.join(IMAGE_DIR, filename)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return filename
    return None


@stuffs_bp.route('/', methods=['GET'])
def get_stuffs():
    """获取所有商品信息，包含完整的图片URL"""
    stuffs = Stuff.query.all()
    result = []

    for stuff in stuffs:
        # 获取商品的基本信息
        stuff_data = stuff_schema.dump(stuff)

        # 查找对应的图片文件
        image_filename = find_image_file(stuff.image_res_id)

        if image_filename:
            # 构建完整的图片URL，包含文件名和后缀
            stuff_data['image_url'] = f"http://127.0.0.1:5000/stuffs/images/{image_filename}"

        result.append(stuff_data)

    return jsonify(result), 200


@stuffs_bp.route('/<int:stuff_id>', methods=['GET'])
def get_stuff(stuff_id):
    """根据ID获取单个商品信息"""
    stuff = Stuff.query.get_or_404(stuff_id)

    # 查找对应的图片文件
    image_filename = find_image_file(stuff.image_res_id)

    if image_filename:
        # 构建完整的图片URL，包含文件名和后缀
        stuff_data = stuff_schema.dump(stuff)
        stuff_data['image_url'] = f"http://127.0.0.1:5000/stuffs/images/{image_filename}"
        return jsonify(stuff_data), 200

    # 如果找不到图片，返回原始数据
    return jsonify(stuff_schema.dump(stuff)), 200


@stuffs_bp.route('/images/<filename>', methods=['GET'])
def get_image_stream(filename):
    try:
        # 构建完整的图片路径
        image_path = os.path.join(IMAGE_DIR, filename)

        # 检查文件是否存在
        if not os.path.exists(image_path):
            return jsonify({
                'status': 'error',
                'message': 'Image not found'
            }), 404

        # 检查是否是文件
        if not os.path.isfile(image_path):
            return jsonify({
                'status': 'error',
                'message': 'Not a valid file'
            }), 400

        # 获取文件扩展名，用于设置Content-Type
        ext = os.path.splitext(filename)[1].lower()

        # 根据文件扩展名设置MIME类型
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
                    chunk = f.read(4096)  # 每次读取4KB
                    if not chunk:
                        break
                    yield chunk

        return Response(generate(), content_type=content_type)

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500