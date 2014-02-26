from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hola/')
@app.route('/hola/<nombre>')
def hola(nombre=None):
    return render_template('hola.html', nombre=nombre)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
