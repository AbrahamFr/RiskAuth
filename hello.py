from flask import Flask, request, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f"{escape(username)}'s profile"

@app.route('/hello')
def hello_world():
    return 'Hello, World! from Flask'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.file['the_file']
        f.save('var/www/uploads/' + secure_filename(f.filename))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    