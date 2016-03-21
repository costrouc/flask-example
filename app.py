from flask import Flask, render_template

app = Flask(__name__)

users = [
    {
        'name': 'Chris Ostrouchov',
        'img_url': '/static/img/chris.jpg',
        'email': 'chris.ostrouchov@gmail.com'
    }, { 
        'name': 'Marci Wetsand',
        'img_url': '/static/img/maci.jpg',
        'email': 'maciwhitson@gmail.com'
    }, {
        'name': 'Adam Sizemore',
        'img_url': '/static/img/adam.jpg',
        'email': 'adam@gmail.com'
    }, {
        'name': 'Nikki Hashemian',
        'img_url': '/static/img/nikki.jpg',
        'email': 'nikki@gmail.com'
    }
]

@app.route('/')
def index_view():
    return render_template('home.html')

@app.route('/users')
def users_view():
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)
