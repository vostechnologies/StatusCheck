from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize the status
STATUS = "UNPAID"

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': STATUS})

@app.route('/status', methods=['POST'])
def update_status():
    global STATUS
    STATUS = request.json.get('status')
    return jsonify({'msg': "Status Changed Successfully!", 'status': STATUS})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
