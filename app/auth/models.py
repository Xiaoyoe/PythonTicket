from app import db

# 用户模型，对应数据库中的user表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 用户ID，主键
    username = db.Column(db.String(80), unique=True, nullable=False)  # 用户名，唯一且不能为空
    email = db.Column(db.String(120), unique=True, nullable=False)  # 邮箱，唯一且不能为空
    password = db.Column(db.String(128))  # 密码
    phone = db.Column(db.String(20))  # 用户电话
    address = db.Column(db.Text)  # 用户地址
    is_admin = db.Column(db.Boolean, default=False)  # 是否为管理员

    # 将用户对象转换为字典格式，方便返回JSON
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'is_admin': self.is_admin
        }