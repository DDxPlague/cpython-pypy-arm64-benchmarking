import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

flask_debug = os.environ.get("FLASK_DEBUG", False)

app.config.update({"DEBUG": bool(flask_debug)})


@app.route("/")
def index():
    simple_date = datetime.now()
    return "Hello, World from PyPy 3, Gunicorn and Gevent! {}".format(simple_date.strftime("%Y-%m-%d %H:%M:%S.%f"))
