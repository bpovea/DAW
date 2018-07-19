from flask import Flask, request
app = Flask(__name__)


@app.route('/<username>/')
def show_request(username):
	print(request.headers)
	print(request.method)
	print(request.data)

	for key in request.args.keys():
		print(key+": "+request.args.get(key))

	return 'HTTP Object'

if __name__ == '__main__':
    app.run(debug=True, port=5000)