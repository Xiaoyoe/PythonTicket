from app import ma
from .models import Stuff
from marshmallow import fields

class StuffSchema(ma.SQLAlchemyAutoSchema):
    image_url = fields.Method("get_image_url")

    class Meta:
        model = Stuff
        load_instance = True

    def get_image_url(self, obj):
        return obj.get_image_url()

# 实例化序列化器
stuff_schema = StuffSchema()
stuffs_schema = StuffSchema(many=True)