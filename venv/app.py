from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/api/v1/hello-world-14")
def hello_world():
    return "Hello World 14"


server_gevent = WSGIServer(('127.0.0.1', 5000), app)
server_gevent.serve_forever()