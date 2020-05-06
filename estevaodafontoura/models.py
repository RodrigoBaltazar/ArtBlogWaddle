from estevaodafontoura.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Post(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(140))
    #price = db.Column(db.Numeric())
    description = db.Column(db.Text)