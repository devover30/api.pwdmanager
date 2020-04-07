from flask import Blueprint, request, jsonify
from pwd_manager.models import *
from exceptions import exception


addUser_blueprint = Blueprint('addUser_blueprint', __name__)

keysList = ['website_name','login_id','login_pwd']

@addUser_blueprint.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        req = request.get_json()
        for key in req.keys():
            outerKey = key
            if outerKey not in keysList:
                raise exception.JsonBadRequest({'error': 'Invalid key', 'allowed keys': keysList})
        data = user_info(website_app_name=req['website_name'], user_name=req['login_id'], login_pwd=req['login_pwd'])
        db.session.add(data)
        db.session.commit()
        return jsonify({"Success": "Action Completed Successfully"}), 201
