from flask import Flask
from flask import render_template
import numpy as np
import json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/api/aircond/co2")
def api():
    data = list(np.random.random(10)*20)
    # print(str(data[0]))
    print(data)
    return {'co2': data}
    # return json.dumps({'co2': 'a'})
    # return 'abc'


@ app.route("/index")
def index():
    return render_template('abc/main.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9999)
