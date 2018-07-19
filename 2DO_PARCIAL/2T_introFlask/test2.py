from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>/')
def show_user_profile(username):
	return '¡Bienvenido, %s!' % username


#debug=True
if __name__ == '__main__':
    app.run(debug=True, port=5000)