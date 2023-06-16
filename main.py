from flask import Flask

from models.pub_key import PublicKeys

app = Flask(__name__)

@app.route('/')
def get_keys():
    return ''

@app.route('/', methods = ['POST'])
def add_key():
    return ''

@app.route('/verify')
def test_keys():
    return True

