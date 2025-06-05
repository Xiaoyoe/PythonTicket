from flask import Blueprint, jsonify, Response
import os

# 创建测试蓝图
test_bp = Blueprint('test', __name__)

# 图片存储目录（根据实际情况修改）
IMAGE_DIR = 'static/images'  # 例如: '/path/to/your/images' 或 'static/images'


@test_bp.route('/images/<filename>', methods=['GET'])
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