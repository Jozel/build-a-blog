from flask import Flask, request, redirect, render_template,session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog2:Cookie1981@localhost:8889/build-a-blog2'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = "super secret key"

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180))
    body = db.Column(db.String(1000))
    

    def __init__(self, title, body ):
        self.title = title
        self.body = body
        


@app.route('/', methods=['GET', 'POST'])
def new_entry():
    

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        print(body)
        new_entry = Blog(title, body) 
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/blog')
    
    return render_template('new_entry.html')

@app.route('/blog', methods=['GET'])
def blog():
     blog_id = request.args.get('id')
     return render_template('main_blog.html', blog=blog)
    # if blog_id:
        #blog_id = request.args.get('id')
       # blog = Blog.query.get(blog_id)

    

if __name__ == '__main__':
    app.run()