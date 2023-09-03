from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='../frontend')
CORS(app)  # CORS有効化

@app.route("/chat", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "Hello World"}
		return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True, port=8888)



