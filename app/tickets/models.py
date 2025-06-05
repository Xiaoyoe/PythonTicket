from app import db

# 复用已有TicketTypeEnum（若需独立定义可复制到此处）
# class TicketTypeEnum(db.Enum):
#     def __init__(self):
#         super().__init__('MOVIE', 'CONCERT', 'MUSIC', 'COMEDY', name='ticket_type')

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('MOVIE', 'CONCERT', 'MUSIC', 'COMEDY'), nullable=False)  # 直接使用枚举值
    title = db.Column(db.String(200), nullable=False)
    image_res_id = db.Column(db.String(50))
    score = db.Column(db.String(50))
    content1 = db.Column(db.Text)
    content2 = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'image_res_id': self.image_res_id,
            'score': self.score,
            'content1': self.content1,
            'content2': self.content2,
            'price': self.price,
            'image_url': self.get_image_url()
        }

    def get_image_url(self):
        if self.image_res_id:
            # 修改为图片流接口的 URL
            return f'http://127.0.0.1:5000/tickets/images/{self.image_res_id}'
        return None