from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from app import db
from .models import Ticket
from .schemas import ticket_schema, tickets_schema

# 创建 tickets 蓝图
tickets_bp = Blueprint('tickets', __name__)


@tickets_bp.route('/', methods=['GET'])
def get_tickets():
    """获取所有票务信息（支持类型过滤）"""
    ticket_type = request.args.get('type')
    query = Ticket.query

    if ticket_type:
        valid_types = ['MOVIE', 'CONCERT', 'MUSIC', 'COMEDY']
        if ticket_type not in valid_types:
            raise BadRequest('Invalid ticket type')
        query = query.filter_by(type=ticket_type)

    tickets = query.all()
    return jsonify(tickets_schema.dump(tickets)), 200


# 根据ID获取单个票务信息
@tickets_bp.route('/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    return jsonify(ticket_schema.dump(ticket)), 200


# 根据type获取对应票务信息
@tickets_bp.route('/<string:ticket_type>', methods=['GET'])
def get_tickets_by_type(ticket_type):
    valid_types = ['movie', 'concert', 'music', 'comedy']
    if ticket_type not in valid_types:
        raise BadRequest('Invalid ticket type')

    tickets = Ticket.query.filter_by(type=ticket_type).all()

    if not tickets:
        return jsonify({"message": f"No tickets found for type {ticket_type}"}), 404

    return jsonify(tickets_schema.dump(tickets)), 200


## 管理员需要进行的增删改
# 创建新票务
@tickets_bp.route('/', methods=['POST'])
def create_ticket():
    data = request.get_json()

    # 验证必要字段
    required_fields = ['type', 'title']
    for field in required_fields:
        if field not in data:
            raise BadRequest(f"Missing required field: {field}")

    # 验证类型
    if data['type'] not in ['MOVIE', 'CONCERT', 'MUSIC', 'COMEDY']:
        raise BadRequest('Invalid ticket type')

    # 创建新票务
    new_ticket = Ticket(
        type=data['type'],
        title=data['title'],
        image_res_id=data.get('image_res_id'),
        score=data.get('score'),
        content1=data.get('content1'),
        content2=data.get('content2'),
        price=data.get('price')
    )

    db.session.add(new_ticket)
    db.session.commit()

    return jsonify(ticket_schema.dump(new_ticket)), 201


# 更新票务信息
@tickets_bp.route('/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.get_json()

    # 更新允许修改的字段
    if 'type' in data:
        if data['type'] not in ['MOVIE', 'CONCERT', 'MUSIC', 'COMEDY']:
            raise BadRequest('Invalid ticket type')
        ticket.type = data['type']

    if 'title' in data:
        ticket.title = data['title']

    if 'image_res_id' in data:
        ticket.image_res_id = data['image_res_id']

    if 'score' in data:
        ticket.score = data['score']

    if 'content1' in data:
        ticket.content1 = data['content1']

    if 'content2' in data:
        ticket.content2 = data['content2']

    if 'price' in data:
        ticket.price = data['price']

    db.session.commit()

    return jsonify(ticket_schema.dump(ticket)), 200


# 删除票务
@tickets_bp.route('/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    db.session.delete(ticket)
    db.session.commit()

    return jsonify({"message": "Ticket deleted successfully"}), 200