import flask
from flask import request, jsonify
from blueprint import bp

app = flask.Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(bp)
app.run()
