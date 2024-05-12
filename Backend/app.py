from realtime_recognition import real_time_recognition, stop_thread
from flask import Flask, jsonify, request
import threading
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

# Keep track of the thread
thread = None

@app.route('/start-recognition', methods=['POST'])
def start_recognition():
    global stop_thread, thread
    stop_thread = False
    if thread is None or not thread.is_alive():
        thread = threading.Thread(target=real_time_recognition)
        thread.start()
    return jsonify({'message': 'Recognition started'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
