from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import secrets



secret_key = secrets.token_hex(16)
print(secret_key)
class ReviewForm(FlaskForm):
    user_name = StringField('Your Name', validators=[DataRequired()])
    review_content = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit Review')
