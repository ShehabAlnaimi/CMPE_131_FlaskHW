from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
#from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired

class TopCitiesForm(FlaskForm):
    city_name = StringField('City Name', validators = [DataRequired()])
    city_rank = IntegerField('City Rank', validators = [DataRequired()])
    is_visited = BooleanField('Visited')
    submit = SubmitField('Submit')


