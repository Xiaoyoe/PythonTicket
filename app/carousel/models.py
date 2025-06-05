from app import db

class Carousel(db.Model):
    __tablename__ = 'carousel'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    image_res_id = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image_url': self.get_image_url(),
            'image_res_id': self.image_res_id
        }

    def get_image_url(self):
        if self.image_res_id:
            return f'http://127.0.0.1:5000/carousels/images/{self.image_res_id}'
        return self.image_url