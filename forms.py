from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ExpenseForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Food', 'Food'), ('Entertainment', 'Entertainment'), ('Utilities', 'Utilities')])
    description = TextAreaField('Description')
    submit = SubmitField('Add Expense')
