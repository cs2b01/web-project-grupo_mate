from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/users', methods = ['GET'])
def get_users():
    session = db.getSession(engine)
    dbResponse = session.query(entities.User)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/users/<id>', methods = ['GET'])
def get_user(id):
    db_session = db.getSession(engine)
    users = db_session.query(entities.User).filter(entities.User.id == id)
    for user in users:
        js = json.dumps(user, cls=connector.AlchemyEncoder)
        return  Response(js, status=200, mimetype='application/json')

    message = { 'status': 404, 'message': 'Not Found'}
    return Response(message, status=404, mimetype='application/json')

@app.route('/users', methods = ['DELETE'])
def delete_user():
    id = request.form['key']
    session = db.getSession(engine)
    messages = session.query(entities.User).filter(entities.User.id == id)
    for message in messages:
        session.delete(message)
    session.commit()
    return "Deleted Message"

@app.route('/users', methods = ['POST'])
def create_user():
    message = json.loads(request.data)
    username = message['username']
    # 2. look in database
    db_session = db.getSession(engine)

    user = db_session.query(entities.User
        ).filter(entities.User.username == username
        ).first()

    if user != None:
        return 'NOT'

    else:
        c = json.loads(request.data)
        user = entities.User(
            username=c['username'],
            name=c['name'],
            fullname=c['fullname'],
            password=c['password']
        )
        session = db.getSession(engine)
        session.add(user)
        session.commit()
        return 'OK'

@app.route('/users', methods = ['PUT'])
def update_user():
    session = db.getSession(engine)
    id = request.form['key']
    user = session.query(entities.User).filter(entities.User.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(user, key, c[key])
    session.add(user)
    session.commit()
    return 'Updated User'

#--------------------------------------------------------------------------

@app.route('/bussiness', methods = ['GET'])
def get_bussiness():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Bussiness)
    data = []
    for bussiness in dbResponse:
        data.append(bussiness)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/bussiness', methods = ['DELETE'])
def delete_bussiness():
    id = request.form['key']
    session = db.getSession(engine)
    bussinesses = session.query(entities.Bussiness).filter(entities.Bussiness.id == id)
    for bussiness in bussinesses:
        session.delete(bussiness)
    session.commit()
    return "Deleted Bussiness"

@app.route('/bussiness', methods = ['POST'])
def create_bussiness():
    message = json.loads(request.data)
    bussiness_name = message['bussiness_name']
    # 2. look in database
    db_session = db.getSession(engine)

    bussiness = db_session.query(entities.Bussiness
        ).filter(entities.Bussiness.bussiness_name == bussiness_name
        ).first()

    if bussiness != None:
        return 'NOT'

    else:
        c = json.loads(request.data)
        bussiness = entities.Bussiness(
            bussiness_name=c['bussiness_name'],
            bussiness_email=c['bussiness_email'],
            bussiness_number=c['bussiness_number'],
            bussiness_description=c['bussiness_description']
        )
        session = db.getSession(engine)
        session.add(bussiness)
        session.commit()
        return 'OK'

@app.route('/bussiness', methods = ['PUT'])
def update_bussiness():
    session = db.getSession(engine)
    id = request.form['key']
    bussiness = session.query(entities.Bussiness).filter(entities.Bussiness.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(bussiness, key, c[key])
    session.add(bussiness)
    session.commit()
    return 'Updated Bussiness'

@app.route('/authenticate', methods = ["POST"])
def authenticate():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    #2. look in database
    db_session = db.getSession(engine)
    try:
        user = db_session.query(entities.User
            ).filter(entities.User.username == username
            ).filter(entities.User.password == password
            ).one()
        session['logged_user'] = user.id
        message = {'message': 'Authorized'}
        return Response(message, status=200, mimetype='application/json')
    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')

@app.route('/current', methods = ["GET"])
def current_user():
    db_session = db.getSession(engine)
    user = db_session.query(entities.User).filter(
        entities.User.id == session['logged_user']
        ).first()
    return Response(json.dumps(
            user,
            cls=connector.AlchemyEncoder),
            mimetype='application/json'
        )

@app.route('/logout', methods = ["GET"])
def logout():
    session.clear()
    return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
