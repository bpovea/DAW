from flask import Flask, json, Response
app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    print(resp.data)
    print(resp.headers)

    return resp

if __name__ == '__main__':
    app.run(debug=True, port=5000)