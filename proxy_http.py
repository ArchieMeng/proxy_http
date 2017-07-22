from flask import Flask, request, make_response
from requests import Session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/proxy/')
def proxy_http():
    if request.method == 'GET':
        url = request.args.get('url', default=None)
        if url:
            for key in request.args:
                if key != 'url':
                    url += "&{key}={value}".format(key=key, value=request.args.get(key))
            response = Session().get(url)
            print url
            return response.content
        else:
            response = make_response(
                (
                    '400 Bad Request: Missing args',
                    400,
                    {}
                )
            )
            return response
    elif request.method == 'POST':
        url = request.args.get('url', default=None)
        if url:
            for key in request.args:
                if key != 'url':
                    url += "&{key}={value}".format(key=key, value=request.args.get(key))
            data = request.form
            response = Session().post(url, data=data)
            return response.content
        else:
            response = make_response(
                (
                    '400 Bad Request: Missing args',
                    400,
                    {}
                )
            )
            return response


if __name__ == '__main__':
    app.run(host='localhost', port=7777, threaded=True)
