#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


# 登录form表单
class LoginForm(Form):
    email = StringField('Email', validators=[Length(1, 64), Email()])# WTForms提供的Length()和Email()验证函数
    password = PasswordField('Password', validators=[])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Length(1, 64), Email()])
    username = StringField('Username', validators=[Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                         'Usernames must have only letters,'
                                                                         'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')



class ChangeEmailForm(Form):
    email = StringField('New Email', validators=[Length(1,64), Email()])
    password = PasswordField('Password', validators=[])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')




class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[])
    password = PasswordField('New password', validators=[
        EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[])
    submit = SubmitField('Update Password')





class PasswordResetRequestForm(Form):
    email = StringField('Email', validators=[Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(Form):
    email = StringField('Email', validators=[Length(1, 64), Email()])
    password = PasswordField('New Password', validators=[
        EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')