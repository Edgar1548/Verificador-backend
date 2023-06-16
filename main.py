from flask import Flask, request, render_template
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Residente1548@localhost/verificador'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True)
    public_key = db.Column(db.String(254))

    def __init__(self, email, public_key):
        self.email = email
        self.public_key = public_key


with app.app_context():
    db.create_all()

@app.route('/')
def get_keys():
    
    return {'testing': 'OkAppProfile'}


@app.route('/api/', methods=['POST'])
def add_key():
    if request.method == 'POST':
        email = request.form.get('email')
        public_key = request.form.get('public_key')
    if db.session.query(Profiles).filter(Profiles.email == email).count() == 0:
        profile = Profiles(email, public_key)
        db.session.add(profile)
        db.session.commit()
    return {'OK': 'Woriking'}


@app.route('/api/verify')
def test_keys():
    if request.method == 'GET':
        dataJsonFormat = request.get_json()
        profiles = Profiles.query.all()
        for data in dataJsonFormat:
            result = next(
                (obj for obj in profiles if obj.email == data['email']),
                None
            )
            if result.public_key != data['public_key']:
                return {'OK': 'IsNotWorking'}
            else:
                continue

    # allProfiles = db.session
    return {'Ok': 'IsWorking'}


if __name__ == '__main__':
    app.run()
