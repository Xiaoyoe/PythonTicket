from app import db

class Stuff(db.Model):
    __tablename__ = 'stuffs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_res_id = db.Column(db.String(50))
    points = db.Column(db.Integer, nullable=False)  # 根据txt文件，points为整数

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_res_id': self.image_res_id,
            'points': self.points,
            'image_url': self.get_image_url()
        }

    def get_image_url(self):
        if self.image_res_id:
            # 修改为图片流接口的 URL
            return f'http://127.0.0.1:5000/stuffs/images/{self.image_res_id}'
        return None