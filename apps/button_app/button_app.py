from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
# api clock_app endpoint url
clock_app_url = os.getenv("CLOCK_APP_URL", "http://clock_app")

@app.route('/')
def index():
    return render_template('button_index.html')

@app.route('/subtract_minutes', methods=['POST'])
def subtract_minutes():
    # get minutes input from html file
    minutes_to_sub = int(request.form['minutes']) 

    # make API call to clock_app to subtract time
    response = requests.post(f'{clock_app_url}/update_time', data={'minutes': minutes_to_sub})

    # check response
    if response.status_code == 200:
        return 'Time subtracted!'
    else:
        return 'Failed to subtract time!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)