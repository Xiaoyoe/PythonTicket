from flask import Blueprint, jsonify, request, Response
from werkzeug.exceptions import BadRequest
from app.carousel.models import Carousel
from app.carousel.schemas import carousel_schema
import os

# 创建 carousels 蓝图
carousels_bp = Blueprint('carousels', __name__)

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


@carousels_bp.route('/', methods=['GET'])
def get_carousels():
    """获取所有轮播图信息，包含完整的图片URL"""
    carousels = Carousel.query.all()
    result = []

    for carousel in carousels:
        # 获取轮播图的基本信息
        carousel_data = carousel_schema.dump(carousel)

        # 查找对应的图片文件
        image_filename = find_image_file(carousel.image_res_id)

        if image_filename:
            # 构建完整的图片URL，包含文件名和后缀
            carousel_data['image_url'] = f"http://127.0.0.1:5000/carousels/images/{image_filename}"

        result.append(carousel_data)

    return jsonify(result), 200


@carousels_bp.route('/<int:carousel_id>', methods=['GET'])
def get_carousel(carousel_id):
    """根据ID获取单个轮播图信息"""
    carousel = Carousel.query.get_or_404(carousel_id)

    # 查找对应的图片文件
    image_filename = find_image_file(carousel.image_res_id)

    if image_filename:
        # 构建完整的图片URL，包含文件名和后缀
        carousel_data = carousel_schema.dump(carousel)
        carousel_data['image_url'] = f"http://127.0.0.1:5000/carousels/images/{image_filename}"
        return jsonify(carousel_data), 200

    # 如果找不到图片，返回原始数据
    return jsonify(carousel_schema.dump(carousel)), 200


@carousels_bp.route('/images/<filename>', methods=['GET'])
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