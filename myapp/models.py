from myapp import db

from flask_login import UserMixin
#from myapp import login


class TopCities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(64), unique=True, index=True)
    city_rank = db.Column(db.Integer)
    is_visited  = db.Column(db.Boolean, unique=False, default=True)
   

    def __repr__(self):
        return f'<TopCities {self.id}: {self.city_name}>'

