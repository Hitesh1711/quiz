from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField, BooleanField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length , Email,EqualTo, email_validator, ValidationError
from flaskblog.model import User
from flask_login import current_user
class RegistrationForm (FlaskForm):
    username= StringField("Username",
        validators=[DataRequired(),Length(min=2,max=15)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField("Sign up")  
    
    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username Already taken!!")

    def validate_email(self,email):
        user= User.query.filter_by(email=email.data.lower()).first()
        if user:
            raise ValidationError("Email Already taken!!")

class LoginForm (FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    remember=BooleanField("Remember Me")
    submit=SubmitField("Sign In")  

class UpdateAccountForm(FlaskForm):
    username= StringField("Username",
        validators=[DataRequired(),Length(min=2,max=15)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    picture= FileField("Update Profile Pic",validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField("Update")  
    
    def validate_username(self,username):
        if username.data!=current_user.username:
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username Already taken!!")

    def validate_email(self,email):
        if email.data!=current_user.email:
            user= User.query.filter_by(email=email.data.lower()).first()
            if user:
                raise ValidationError("Email Already taken!!")