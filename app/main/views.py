from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required, current_user
from .. import auth
from ..models import User,Blog,Comments
from .forms import UpdateProfile, BlogForm, CommentPitch
from .. import db,photos



#views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'PITCH'

    return render_template('index.html', title = title )   


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)

@main.route('/new/blog',methods = ['GET','POST'])
@login_required
def add_category_blog():
    form = BlogForm()
    blog = Blog.query.filter_by().all()
    if form.validate_on_submit():
        blog = Blog(pitch_title=form.pitch_title.data,user=current_user)
        db.session.add(blog)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('blog.html',category_form = form,blog=blog)

@main.route('/posted/blogs',methods = ['GET','POST'])
@login_required
def posted_blogs():
    form = BlogForm()
    blog = Blog.query.filter_by().all()
    if form.validate_on_submit():
        blog = Blog(pitch_title=form.pitch_title.data,user=current_user)
        db.session.add(blog)
        db.session.commit()
        flash('It ahs been posted to posted blogs')    
        return redirect(url_for('.index'))
    return render_template('posted_blogs.html',category_form = form,blog=blog)

@main.route('/comment/blog',methods = ['GET','POST'])
@login_required
def add_comment_blog():
    form = CommentPitch()
    comment = Comments.query.filter_by().all()
    if form.validate_on_submit():
        comment = Comments(comment_title=form.comment_title.data)
        db.session.add(comment)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('blog.html',category_form = form,comment=comment)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
