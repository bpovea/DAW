from flask import Flask, json, Response, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/procesar', methods = ['GET','POST'])
def procesar():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form.get('nombre')  # access the data inside 
        apellido = request.form.get('apellido')
        if nombre == 'admin' and apellido == 'admin':
            mensaje = "Usuario y contraseña correctas"
        else:
            mensaje = "Usuario o contraseña incorrectas"

    return render_template('formulario.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True, port=5000)