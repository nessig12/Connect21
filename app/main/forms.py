from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User, Topics


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    # choices = []
    # topics = Topics.query.all()
    # for topic in topics: 
    #     choices += [topics.topic]
    #tag = SelectField(u'Topics')
    #tag = SelectField(u'Tags', choices = [(g.id, g.topic) for g in Topics.query.order_by('topic')])
    tag = SelectField(u'Tags', choices=[('Sports','Sports'),('Life with Down Syndrome','Life with Down Syndrome'), ('TV Shows/Movies','TV Shows/Movies'),('Cooking','Cooking'), ('Funny Memes','Funny Memes'),('Puzzles','Puzzles'),('Scary Stories','Scary Stories'),('Politics','Politics'),('Dream Job','Dream Job')])
    submit = SubmitField(_l('Submit'))

    # def tag_help(request):
    #     topic_choices = Topics.query.order_by('topic')
    #     print("helooooooooooooo")
    #     print(topic_choices)
    #     form = PostForm(request.POST, obj=topic_choices)
    #     form.tag.choices = [(g.id,g.topic) for g in Topics.query.order_by('topic')]

# class UserDetails(Form):
#     group_id = SelectField(u'Group')

#     def edit_user(request, id):
#         topics = Topics.query.get(id)
#         form = PostForm(request.POST, obj=topics)
#         form.tag.choices = [(g.id, g.name) for g in Group.query.order_by('name')]

class AddTopic(FlaskForm): 
    topic = StringField(_l('New Topic'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
