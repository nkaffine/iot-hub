import socket
from flask import Flask
from flask import request
import threading
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "hello world"


if __name__ == "__main__":
    app.run()
