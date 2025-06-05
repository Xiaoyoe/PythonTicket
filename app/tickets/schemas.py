from app import ma
from .models import Ticket
from marshmallow import fields

class TicketSchema(ma.SQLAlchemyAutoSchema):
    # 使用 Method 字段来生成 image_url
    image_url = fields.Method("get_image_url")

    class Meta:
        # 指定对应的模型
        model = Ticket
        # 允许将反序列化的数据加载为模型实例
        load_instance = True

    def get_image_url(self, obj):
        # 调用 Ticket 模型的 get_image_url 方法获取图片 URL
        return obj.get_image_url()

# 实例化单个 Ticket 对象的序列化器
ticket_schema = TicketSchema()
# 实例化多个 Ticket 对象的序列化器
tickets_schema = TicketSchema(many=True)