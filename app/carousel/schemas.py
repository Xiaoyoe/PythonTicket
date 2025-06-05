from app import ma
from .models import Carousel
from marshmallow import fields

class CarouselSchema(ma.SQLAlchemyAutoSchema):
    image_url = fields.Method("get_image_url")

    class Meta:
        model = Carousel
        load_instance = True

    def get_image_url(self, obj):
        return obj.get_image_url()

# 实例化序列化器
carousel_schema = CarouselSchema()
carousels_schema = CarouselSchema(many=True)