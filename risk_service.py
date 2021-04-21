"""Risk Service to dynamically enforce types of authentication"""

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from risk_values import LogInformation

app = Flask(__name__)
log_info = LogInformation('./logs')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    """Save log file"""
    if request.method == 'POST':
        print(request.files)
        f = request.files['fileUpload']
        file_path = './logs/' + secure_filename(f.filename)
        f.save(file_path)
        log_info.addLog(file_path)
        return "logged it"
    else:
        return render_template('log.html')

@app.route('/risk')
def risk():
    return render_template('risk.html')

@app.route('/risk/isuserknown/<username>')
def is_user_known(username):
    return f"{log_info.is_user_known(username)}".lower()

@app.route('/risk/isclientknown/<client>')
def is_client_known(client):
    return f"{log_info.is_client_known(client)}".lower()

@app.route('/risk/isipknown/<ip>')
def is_ip_known(ip):
    return f"{log_info.is_ip_known(ip)}".lower()

@app.route('/risk/isipinternal/<ip>')
def is_ip_internal(ip):
    return f"{log_info.is_ip_internal(ip)}".lower()


@app.route('/risk/failedlogincountlastweek')
def failed_login_count_lastweek():
    return "4"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('log'))
    print(url_for('risk'))

with app.test_request_context('/log', method='POST'):
    assert request.path == '/log'
    assert request.method == 'POST'
