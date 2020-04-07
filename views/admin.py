from flask import Blueprint, request, jsonify
from pwd_manager.models import *
from exceptions import exception


admin_blueprint = Blueprint('admin_blueprint', __name__)

keysList = ['website_name','login_id','login_pwd']

@admin_blueprint.route('/admin/edit/<int:id>', methods=['PATCH'])
def edit_user(id):
    user = user_info.query.filter_by(id=id).first()
    if not user:
        raise exception.JsonUnprocessable({"Error": "Cant Find Specified ID"})
    if request.method == 'PATCH':
        req = request.get_json()
        for key in req.keys():
            outerKey = key
            if outerKey not in keysList:
                raise exception.JsonBadRequest({'error': 'Invalid key', 'allowed keys': keysList})
        user.website_app_name = req['website_name']
        user.user_name = req['login_id']
        user.login_pwd = req['login_pwd']
        db.session.commit()
        return jsonify({"success": "User info Successfully edited"})



@admin_blueprint.route('/admin/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = user_info.query.filter_by(id=id).first()
    if not user:
        raise exception.JsonUnprocessable({"Error": "Cant Find Specified ID"})
    if request.method == 'DELETE':
        req = request.get_json()
        for key in req.keys():
            outerKey = key
            if outerKey not in keysList:
                raise exception.JsonBadRequest({'error': 'Invalid key', 'allowed keys': keysList})
        db.session.delete(user)
        db.session.commit()
        return jsonify({}), 204

