from flask import Flask
from app.helpers import get_greeting

app = Flask(__name__)


@app.route('/hello/<name>', methods=['GET'])
def hello_world(name):
    """
    render a greeting
    :param name: string
    :return: Flask Request
    """
    return get_greeting(name)
