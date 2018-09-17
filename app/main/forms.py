from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    pitch_title=TextAreaField('Write a blog title', validators=[Required()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    pitch_title = TextAreaField('Write a category', validators=[Required()])
    submit = SubmitField('Submit')

class CommentPitch(FlaskForm):
    comment_title = TextAreaField('Write a comment',validators=[Required()])
    submit = SubmitField('Comment')
