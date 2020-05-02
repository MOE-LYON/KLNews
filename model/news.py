from datetime import datetime

from . import db


class News(db.Model):
    __tablename__="news"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    front_image = db.Column(db.String(60), nullable=False)

    category = db.relationship('Category',
                               backref=db.backref('news', lazy=True))

    def to_json(self):
        return {
            'id':self.id,
            'title':self.title,
            'publish_date':self.pub_date,
            'cid':self.category_id,
            'front_image':self.front_image,
            'content':self.body
        }