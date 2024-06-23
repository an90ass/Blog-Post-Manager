from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,BooleanField,ValidationError
from wtforms.validators import DataRequired,EqualTo,Length
from wtforms.widgets import TextArea
class NamerForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    name = StringField("Enter Your Name",validators=[DataRequired()])
    user_name = StringField("Enter User Name",validators=[DataRequired()])
    email= StringField("Enter Your Email",validators=[DataRequired()])
    favorite_color = StringField("Enter Your Favoraite Color")
    password_hash = PasswordField("Enter Your Password",validators=[DataRequired(),EqualTo('password_hash2',message='Passwords Must Match')])
    password_hash2 = PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField("Submit")

class PasswordForm(FlaskForm):
    email= StringField("Enter Your Email",validators=[DataRequired()])
    password_hash= PasswordField("Enter Your Password",validators=[DataRequired()])
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired()])
    content = StringField("Content",validators=[DataRequired()],widget=TextArea())
    author = StringField("Author")
    slug = StringField("Slug",validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    user_name = StringField("User Name",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Login")

class SearchForm(FlaskForm):
    searched = StringField("Searched",validators=[DataRequired()])
    submit = SubmitField("search")



