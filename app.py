from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    request_data = request.get_json()
    input_str = request_data['input_str']
    processed_str = input_str.upper()
    return {'output_str': processed_str}
