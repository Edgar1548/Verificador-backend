from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db= SQLAlchemy(app)


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(254))
    public_key = db.Column(db.String(254))
    def __init__(self, email, public_key) -> None:
        self.email = email
        self.public_key = public_key

@app.route('/api')
def get_keys():
    return ''

@app.route('/api', methods = ['POST'])
def add_key():
    return ''
    
@app.route('/verify')
def test_keys():
    return ''

