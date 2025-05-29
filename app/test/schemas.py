from app import ma
from app.auth.models import User

# 用户序列化模式，使用 SQLAlchemyAutoSchema 自动映射模型字段
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # 允许反序列化回对象
        fields = ('id', 'username', 'email', 'phone', 'address', 'is_admin')

# 创建单用户和多用户的序列化器实例
user_schema = UserSchema()  # 用于单个用户
users_schema = UserSchema(many=True)  # 用于用户列表