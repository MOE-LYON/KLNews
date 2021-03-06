from . import db


class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False,unique=True)
    description = db.Column(db.String(100))

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description
        }