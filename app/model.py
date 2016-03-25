from _init_ import db 
class Thumbnail(db.Model):
    __tablename__ = 'thumbnail'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(100), index = True)