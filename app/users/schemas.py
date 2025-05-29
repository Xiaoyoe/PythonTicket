from app import ma
from app.auth.models import User

# 用户资料序列化模式，使用 SQLAlchemyAutoSchema 自动映射模型字段
class UserProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # 允许反序列化回对象
        fields = ('id', 'username', 'email', 'phone', 'address')

# 创建用户资料序列化器实例
user_profile_schema = UserProfileSchema()