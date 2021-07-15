from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer= Freezer(app)
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

# ---------------------------setup webapp structure/routing----------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def downloadPage():
    return render_template('download.html')

if __name__ == '__main__':
    freezer.run()
