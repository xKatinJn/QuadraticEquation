from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class SolverForm(FlaskForm):
    a_value = StringField('a_value', validators=[DataRequired()])
    b_value = StringField('b_value', validators=[DataRequired()])
    c_value = StringField('c_value', validators=[DataRequired()])
    submit = SubmitField('Решить')
