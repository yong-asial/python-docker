from flask import Flask
import threading
import sys
import os
import train as fib

app = Flask(__name__)

status = 0

def output(msg):
    print(msg, file=sys.stderr)
    print(msg, file=sys.stdout)


def my_threaded_func(arg, arg2):
    output("Running thread! Args:")
    fib.start()
    output("Thread Done!")


def task():
    thread = threading.Thread(target=my_threaded_func, args=("I'ma", "thread"))
    thread.start()
    output("Spun off thread")
    return True

def validToken(token):
    if token is None:
        return False
    if token != os.getenv("AUTHORIZED_TOKEN"):
        return False
    return True

@app.route('/')
def index():
    task()
    return 'Index Page'

@app.route('/start/<token>')
def start(token):
    if not validToken(token):
        return 'Invalid Access'
    return 'Start'
