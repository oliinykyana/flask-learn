from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Yana'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home Page', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Log In', form=form)
