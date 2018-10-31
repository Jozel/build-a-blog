from flask import Flask, request, redirect, render_template,session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog2:Cookie1981@localhost:8889/build-a-blog2'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    

    def __init__(self, title, body=True):
        self.title = title
        self.body = body
        


@app.route('/', methods=['POST', 'GET'])
def new_post():
    form = BlogForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('newpost.html', form=form)
        else:

            owner = User.query.filter_by(username=session['username']).first()
            blog_title = form.blog_title.data
            blog_post = form.blog_post.data

            new_blog = Blog(blog_title, blog_post, owner)
            db.session.add(new_blog)
            db.session.commit()

            return redirect(url_for('blog', id=new_blog.id))

    return render_template('newpost.html', form=form, title="Add a Blog Entry")


@app.route('/delete-task', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()