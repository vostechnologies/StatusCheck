from flask import Flask, jsonify, request
import json

app = Flask(__name__)

STATUS_FILE = "status.json"

def read_status():
    try:
        with open(STATUS_FILE, 'r') as f:
            status_data = json.load(f)
        return status_data.get('status', 'ERROR')
    except FileNotFoundError:
        return 'ERROR'

def write_status(status):
    with open(STATUS_FILE, 'w') as f:
        json.dump({'status': status}, f)

STATUS = read_status()

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': STATUS})

@app.route('/status', methods=['POST'])
def update_status():
    global STATUS
    new_status = request.json.get('status')
    check = request.json.get('check')
    if (check == "69420"):
        STATUS = new_status
        write_status(new_status)
        return jsonify({'msg': "Status Changed Successfully!", 'status': STATUS})
    else:
        return jsonify({'msg': "Invalid Check!"})

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5050)
