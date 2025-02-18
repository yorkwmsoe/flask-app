from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello MSOE'

@app.get('/calculate')
def calculate():
    op = request.args.get('operator')
    arg1 = int(request.args.get('arg1'))
    arg2 = int(request.args.get('arg2'))
    if op == 'add':
        return str(arg1 + arg2)
    elif op == 'sub':
        return str(arg1 - arg2)
    elif op == 'mult':
        return str(arg1 * arg2)
    elif op == 'div':
        return str(arg1 / arg2)
    else:
        return 'Not supported'
