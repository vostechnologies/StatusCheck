from flask import Flask, jsonify

app = Flask(__name__)

# Initialize the status
STATUS = True

# Endpoint to get the status
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': STATUS})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
