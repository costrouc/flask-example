from flask import Flask, render_template, request, redirect, url_for, session

from data import users, feed

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def home_view():
    return render_template('home.html')


@app.route('/users')
def users_view():
    return render_template('users.html', users=users)


@app.route('/user/<user_id>')
def user_view(user_id):
    if user_id in users:
        return render_template('user.html', user=users[user_id])
    return redirect(url_for('page_not_found'))


@app.route('/feed')
def feed_view():
    # TODO: Add user url to dictionary
    return render_template('feed.html', feed=feed)


@app.route('/signup', methods=['GET', 'POST'])
def signup_view():
    if request.method == 'GET':
        return render_template('signup.html')
    else: # POST request
        # TODO: BAD trusting user input and NEVER
        #       store password plaintext
        new_user = {
            'username': request.form['Username'],
            'name': request.form['Fullname'],
            'password': request.form['Password'],
            'image': '/static/img/user/default.jpg',
            'email': request.form['Email'],
        }
        users.update({request.form['Username']: new_user})
        return redirect(url_for('home_view'))


@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'GET':
        return render_template('login.html')
    else: # POST request
        for user_id, user in users.items():
            if user['username'] == request.form['Username'] and \
               user['password'] == request.form['Password']:
                session['authenticated'] = True
                session['user_id'] = user_id
                return redirect(url_for('users_view'))
        return redirect(url_for('home_view'))


@app.route('/logout')
def logout_view():
    session['user_id'] = ''
    return redirect(url_for('home_view'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
