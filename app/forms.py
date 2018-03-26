"""
forms.py holds the various classes of form types
The classes are implemented by using flask_wtf and wtforms
Classes:
	LoginForm: class for the login form 
	RegistrationForm: class for the signup/registration form
	ThreadForm: class for creating a new thread
	PostForm: class for creating a post
"""
from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import SubmitField,StringField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
=======
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import InputRequired, Email, Length, DataRequired

>>>>>>> master

class LoginForm(FlaskForm):
    """
    LoginForm is the class which creates the forms and variables for logging in a user.
    fields:
        username: StringField which takes in the a users username
        password: PasswordField which takes in a users password
        remember: BooleanField which creates a box a user can check to stay logged in

        Username and Password fields have InputRequired and Length constraints.
    """
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=80)])
    remember = BooleanField('Remember Me')


class RegistrationForm(FlaskForm):
    """
    RegistrationForm is the class which creates the forms and variables for signing up a user.
    fields:
        email: StringField which takes in a users email
        username: StringField which takes in the a users username
        password: PasswordField which takes in a users password

        Username and Password fields both have InputRequired and length constraints, and the email field has an email constraint
        which must be in format 'email@test.com'

    """
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class ThreadForm(FlaskForm):
<<<<<<< HEAD
	"""
	ThreadForm is a class which creates the forms and variables for creating a thread.
	Fields:
	    thread: StringField which takes in the topic for a thread
	    post: TextAreaField which takes in the body of a post
    
    Thread and post fields both have InputRequired and length constraints
	"""
	thread = StringField('Title:', validators=[InputRequired(), Length(min=1, max=128)])
	post = TextAreaField('Body:', validators=[InputRequired(), Length(min=1, max=1000)])

class PostForm(FlaskForm):
	"""
	PostForm is a class which creates the forms and variables for creating a post.
	Fields:
	    thread: StringField which takes in the topic for a thread
	    post: TextAreaField which takes in the body of a post
	    submit: SubmitField which validates the post

	    Thread and post fields both have InputRequired and length constraints
    """
	post = TextAreaField('Add a post:', validators=[InputRequired(), Length(min=1, max=1000)])
	submit = SubmitField('Submit')
=======
    thread = StringField('Title:', validators=[InputRequired(), Length(min=1, max=128)])
    post = TextAreaField('Body:', validators=[InputRequired(), Length(min=1, max=1000)])


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class ChangePasswordForm(FlaskForm):
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])

    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')




    

















>>>>>>> master
