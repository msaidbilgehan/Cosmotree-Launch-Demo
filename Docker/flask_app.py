import json
import os

from flask import Flask, jsonify, request, send_from_directory, render_template, Response

from Flask_App.paths import app_path
from Flask_App.Libraries.logger_module import global_logger
from Flask_App.Classes.serial_communication import SerialObject



app = Flask(__name__, template_folder=f'{app_path}frontend/pages', static_folder=f'{app_path}frontend/static')
# serial_object = SerialObject()


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


@app.route('/card',methods = ['POST', 'GET'])
def card():
    """ Card Page for Sensor Data """
    return render_template(
        'card.html',
        page_id="card"
    )


@app.route('/api_serial/',methods = ['POST', 'GET'])
def api_serial():
    """ Serial APU """
    global_logger.info(f'REQUEST INFORMATION > IP: {request.remote_addr}, Route: {request.path}, Params: {request.args.to_dict()}')

    return Response(
        SerialObject.read_yield_simulate(),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'X-Accel-Buffering': 'no' # Disable buffering
        }
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