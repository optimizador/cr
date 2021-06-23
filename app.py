from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dimensionamiento/cloud_pak')
def dim_cp():
    return render_template('dim_cp.html')

if __name__ == "_main_":
    app.run(host="0.0.0.0")
