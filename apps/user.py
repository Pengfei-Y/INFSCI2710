# user_bp
from flask import Blueprint, render_template, request, session, redirect
from sql_config import db_session, User

user_bp = Blueprint('user', __name__)


@user_bp.route('/user/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with db_session():
            res_info = db_session.query(User).filter(User.username == username).filter(
                User.password == password).first()
        if res_info:
            session['user'] = res_info.id

            return '1'
        else:
            return '0'


@user_bp.route('/user/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        eamil = request.form['eamil']
        address = request.form['address']
        userclass = request.form['userclass']
        try:
            with db_session():
                infos = User(username=username, password=password, name=name, email=eamil, address=address,
                             user_class=userclass)
                db_session.add(infos)
                db_session.commit()
                return '1'

        except:
            return '0'


@user_bp.route('/user/userinfo', methods=['POST', 'GET'])
def userinfo():
    if not session.get('user'):
        return redirect('/user/login')

    else:
        if request.method == 'GET':
            with db_session():
                user_infos = db_session.query(User).filter(User.id == int(session['user'])).first()

            username = user_infos.username
            password = user_infos.password
            name = user_infos.name
            balance = user_infos.balance
            address = user_infos.address
            email = user_infos.email
            user_class = user_infos.user_class
            return render_template('user/userinfo.html', username=username, password=password, name=name,
                                   balance=balance, address=address, email=email, user_class=user_class)

        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            name = request.form['name']
            eamil = request.form['eamil']
            address = request.form['address']
            userclass = request.form['userclass']
            print(userclass)

            print(eamil, userclass)
            try:
                with db_session():
                    user_infos = db_session.query(User).filter(User.id == int(session['user'])).first()
                    user_infos.username = username
                    user_infos.password = password
                    user_infos.name = name
                    user_infos.email = eamil
                    user_infos.address = address
                    user_infos.user_class = userclass
                    db_session.commit()
                    db_session.close()
                return '1'
            except:
                return '0'
