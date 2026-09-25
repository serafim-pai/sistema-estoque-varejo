from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Olá! Estou funcionando!'

if __name__ == '__main__':
    print('Iniciando servidor na porta 5000...')
    app.run(debug=True, port=5000)