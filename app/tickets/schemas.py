from app import ma
from .models import Ticket

class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        load_instance = True
        # 排除不需要序列化的字段（如有）
        # exclude = ('content1', 'content2')

# 实例化序列化器
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)