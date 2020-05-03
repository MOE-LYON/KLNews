from . import api_bp
from flask import request, current_app, jsonify
import pathlib
import uuid

@api_bp.route(rule="/upload",methods=["Post"])
def upload():

    save_path =  pathlib.Path.joinpath(current_app.root_path,"static")

    data_file = []
    files = request.files
    for file in files:
        if files[file].filename == '':
            continue
        if files[file]:
            filename = str(uuid.uuid4()) + '.' + files[file].filename.rsplit('.', 1)[1].lower()
            files[file].save(pathlib.Path.joinpath(save_path, filename))
            data_file.append(filename)
    msg = 'success' if len(data_file) else 'error'
    return jsonify({'msg': msg, 'data': data_file, 'code': 200})

