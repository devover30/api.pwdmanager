from flask import Blueprint, request, jsonify, url_for
from pwd_manager.models import *
from exceptions import exception
import requests
from pathlib import Path
import os


addUser_blueprint = Blueprint('addUser_blueprint', __name__)

keysList = ['website_name','login_id','login_pwd','title']

@addUser_blueprint.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        req = request.get_json()
        req = validation(req)
        logo_url = addLogo(req['website_name'], req['title'].lower())
        data = user_info(website_app_name=req['website_name'], title=req['title'],
                         logo=logo_url,user_name=req['login_id'],
                         login_pwd=req['login_pwd'])
        db.session.add(data)
        db.session.commit()
        return jsonify({"Success": "Action Completed Successfully"}), 201


def addLogo(name,title):
    url = f'https://logo.clearbit.com/{name}'
    filename = f'{title}.jpg'
    file_dir = Path.cwd().joinpath(f'pwd_manager/static')
    if not file_dir.exists():
        os.makedirs(str(file_dir))
    header = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    page = requests.get(url,headers=header, stream=True)
    img_data = page.content
    with open(f'{file_dir}/{filename}','wb') as handler:
        handler.write(img_data)
    return f"{request.host_url}static/{filename}"

def validation(data):
    for key in data.keys():
        outerKey = key
        if outerKey not in keysList:
            raise exception.JsonBadRequest({'error': 'Invalid key', 'allowed keys': keysList})
    for k, v in data.items():
        if data[k] is None or data[k] == '':
            raise exception.JsonBadRequest({k: "This is Null"})
    return data
