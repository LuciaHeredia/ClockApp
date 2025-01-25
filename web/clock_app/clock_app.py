from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
current_time = datetime.now()

@app.route('/')
def index():
    return render_template('clock_index.html', 
                           current_time = current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)