from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Record(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    lastname = db.Column(db.String(128))
    phone = db.Column(db.String(48))
    company = db.Column(db.String(256))
    def __repr__(self):
        return f'<Record {self.name}>'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form_page.html')

@app.route('/form/submit', methods=['POST'])
def form_submit():
    name = request.form.get('name', default='err: no data')
    lastname = request.form.get('lastname', default='err: no data')
    phone = request.form.get('phone', default='err: no data')
    company = request.form.get('company', default='err: no data')
    rec = Record(name=name, lastname=lastname, phone=phone, company=company)
    db.session.add(rec)
    db.session.commit()
    return render_template('thanks_page.html')

@app.route('/database')
def get_data():
    recs = Record.query.all()
    return render_template('database.html', records=recs)
