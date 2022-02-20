from models.models import *
from app import app, db
# from app import *
from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for


@app.route('/post',  methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['post']
        post_author = request.form['author']
        new_post = Post(title=post_title,
                        content=post_content, posted_by=post_author)
        db.session.add(new_post)
        db.session.commit()

        return redirect('/post')
    else:
        all_posts = Post.query.order_by(Post.posted_on).all()
        return render_template('post.html', post=all_posts)


@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['post']
        post_author = request.form['author']
        new_post = Post(title=post_title,
                        content=post_content, posted_by=post_author)

        # if request.form['submit_button1'] == 'like':
        #     number1 = 1
        #     return number1
        # elif request.form['submit_button2'] == 'dislike':
        #     number2 = 1
        #     return number2

        db.session.add(new_post)
        db.session.commit()
        return redirect('/post')

    else:
        return render_template('new_post.html')


@app.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    to_edit = Post.query.get_or_404(id)
    if request.method == 'POST':
        to_edit.title = request.form['title']
        to_edit.author = request.form['author']
        to_edit.content = request.form['post']
        db.session.commit()
        return redirect('/post')

    else:
        return render_template('post_edit.html', post=to_edit)


@app.route('/post/delete/<int:id>')
def delete(id):
    to_delete = Post.query.get_or_404(id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect('/post')