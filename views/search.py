from flask import Blueprint, jsonify
from pwd_manager.models import *
import re

search_blueprint = Blueprint('search_blueprint',__name__)

@search_blueprint.route('/search/weblogin/<name>', methods=['GET'])
def search(name):
    data = name.lower()
    rows = user_info.query.with_entities(user_info.id, user_info.website_app_name).all()
    ids = []
    for row in rows:
        string = str(row[0])+row[1].lower()
        result = re.findall(data, string)
        if result:
            ids.append(row[0])
    rows = []
    for i in range(0, len(ids)):
        rows.append(user_info.query.filter_by(id=ids[i]).first())
    response = [row.serialized for row in rows]
    return jsonify({'weblogins':response})
