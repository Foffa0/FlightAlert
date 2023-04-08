from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class AirportForm(FlaskForm):
    query = StringField('Airport', validators=[DataRequired()])
    submit = SubmitField('Speichern')

class AircraftForm(FlaskForm):
    query = StringField('Search Aircraft', validators=[DataRequired()])
    airport_icao = StringField(validators=[DataRequired()])
    search_option = RadioField('', choices=[(1,'aircraft'), (2, 'engine count')], default=1, coerce=int)
    submit = SubmitField('Search')