from flask import Blueprint, jsonify
from pwd_manager.models import *


getall_blueprint = Blueprint('getall_blueprint',__name__)

@getall_blueprint.route('/weblogin', methods=['GET'])
def getAll():
    rows = user_info.query.all()
    response = [row.serialized for row in rows]
    return jsonify({'weblogins':response})