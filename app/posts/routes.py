from flask import Blueprint, render_template, redirect, url_for, abort, request
from flask_security import current_user, login_required

from app.posts.models import Post
from app.posts.forms import PostForm
from app.extensions import db

blueprint = Blueprint('posts', __name__)

@blueprint.route('/')
def home():
    posts = Post.query.all()
    return render_template('posts/home.html', posts= posts, name=current_user.username if current_user.is_authenticated else '')

@blueprint.route('/post/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            content =form.content.data,
            auther = current_user
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.home'))
    return render_template('posts/create.html', form= form) 


@blueprint.route('/post/detail/<int:post_id>')
@login_required
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/detail.html', post = post)

@blueprint.route('/post/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update(post_id):
    post = Post.query.get_or_404(post_id)

    if not(post.auther == current_user or current_user.has_role('admin')):
        abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for('posts.detail', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        
    return render_template('posts/update.html', form=form)

@blueprint.route('/post/delete/<int:post_id>')
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)

    if not(post.auther == current_user or current_user.has_role('admin')):
        abort(403)

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.home'))