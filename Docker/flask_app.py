import json
import os

from flask import Flask, jsonify, request, send_from_directory, render_template, Response

from Flask_App.paths import app_path
from Flask_App.Libraries.logger_module import global_logger



app = Flask(__name__, template_folder=f'{app_path}frontend/pages', static_folder=f'{app_path}frontend/static')



#############
### PAGES ###
#############


@app.route('/',methods = ['POST', 'GET'])
def index():
    global_logger.info(f'REQUEST INFORMATION > IP: {request.remote_addr}, Route: {request.path}, Params: {request.args.to_dict()}')
    
    param1_json = request.args.get('param1')
    if param1_json:
        param1 = json.loads(param1_json)
        global_logger.info(f'PARAMETERS > param1: {param1}')

    return render_template(
        'index.html',
        page_id="index"
    )


@app.route('/fqdn',methods = ['POST', 'GET'])
def fqdn_page():
    global_logger.info(f'REQUEST INFORMATION > IP: {request.remote_addr}, Route: {request.path}, Params: {request.args.to_dict()}')
    
    param1_json = request.args.get('param1')
    if param1_json:
        param1 = json.loads(param1_json)
        global_logger.info(f'PARAMETERS > param1: {param1}')

    return render_template(
        'fqdn.html',
        page_id="fqdn"
    )


@app.route('/about',methods = ['POST', 'GET'])
def about():
    global_logger.info(f'REQUEST INFORMATION > IP: {request.remote_addr}, Route: {request.path}, Params: {request.args.to_dict()}')
    return render_template(
        'about.html',
        page_id="about"
    )


@app.route('/404',methods = ['POST', 'GET'])
def not_found():
    global_logger.info(f'REQUEST INFORMATION > IP: {request.remote_addr}, Route: {request.path}, Params: {request.args.to_dict()}')
    return render_template(
        '404.html',
        page_id="404"
    )


if __name__ == '__main__':
    app.run(
        host=os.getenv("HOST", "0.0.0.0"), 
        port=int(os.getenv("PORT", 5005)), 
        debug = True
    )