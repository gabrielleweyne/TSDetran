from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/tecnologias')
def tecnologias():
    return render_template('tecnologias.html')

@app.route('/parceiros')
def parceiros():
    return render_template('parceiros.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

if __name__ == '__main__':
    app.run(debug=True)
