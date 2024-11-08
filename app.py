from flask import Flask, request # type: ignore
from datetime import datetime

app =Flask(__name__)

@app.route('/')
def hello():
    return  'Hello World'



@app.route('/time')
def time_now():
    if request.args.get('time') == 'now':
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return ({'timenow': current_time})

@app.route('/whoami')
def who_am_i():
    if request.args.get('whoami') == '1':
        client_ip = request.remote_addr
        return {'client_ip': client_ip}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)

