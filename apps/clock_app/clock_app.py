from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
current_time = datetime.now()

@app.route('/')
def index():
    return render_template('clock_index.html', 
                           current_time = current_time)

@app.route('/update_time', methods=['POST'])
def update_time():
    # to modify a global variable inside a function.
    global current_time 
    # get minutes to subtract from button_app POST action
    minutes_to_sub = int(request.form['minutes']) 
    # update time in page: subtract minutes(time in general) between 2 datetime objects.
    current_time -= timedelta(minutes=minutes_to_sub)
    # return a JSON response with the content {"status": "success"} and a HTTP status code of 200, indicating a successful request.
    return jsonify({'status': 'success'}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)