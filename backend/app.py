from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS有効化


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "Hello World"}
		return jsonify(data)

# @app.after_request
# def set_cors_header(response):
#     クライアント側のアドレスとポート = 'http://127.0.0.1:8080'
#     response.headers['Access-Control-Allow-Origin'] = クライアント側のアドレスとポート
#     response.headers['Access-Control-Allow-Method'] = 'GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS'  # noqa: E501
#     response.headers['Access-Control-Allow-Headers'] = 'Content-type,Accept,X-Custom-Header'  # noqa: E501
#     response.headers['Access-Control-Allow-Credentials'] = 'true'
#     response.headers['Access-Control-Max-Age'] = '86400'
#     return response

if __name__ == '__main__':
	app.run(debug=True)
