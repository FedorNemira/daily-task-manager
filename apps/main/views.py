from flask import render_template
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from apps.main.models import User
from apps.main.models import db

main = Blueprint('main', __name__, template_folder="templates")


@main.route('/')
def hello():
    return render_template('base.html')

@main.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        name = data['username']
        email = data['email']
        password = data['password']

        user = User()
        user.username = name
        user.email = email
        user.password_hash = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()

        return jsonify({'success': True, 'active': user.active})


    elif request.method == 'GET':
        users = [user.as_dict() for user in User.query.all()]

        return users

    return render_template('main/register.html')