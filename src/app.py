from flask import Flask, render_template;

flask = Flask(__name__)

if __name__ == '__main__':
    flask.run(debug=True)

@flask.route('/')
def index():
    return render_template('index.html')

@flask.route('/index')
def login():
    return render_template('index.html')

@flask.route('/inicio')
def inicio():
    return render_template('inicio.html')

@flask.route('/clientes')
def clientes():
    return render_template('clientes.html')

@flask.route('/facturas')
def facturas():
    return render_template('facturas.html')

@flask.route('/registro')
def registro():
    return render_template('registro.html')

@flask.route('/cuenta')
def cuenta():
    return render_template('cuenta.html')




