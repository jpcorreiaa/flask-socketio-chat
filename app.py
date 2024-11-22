from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
socketio = SocketIO(app)

# Rota para renderizar o arquivo index.html
@app.route('/chat')
def index():
    return render_template('index.html')

# Função para tratar mensagens do chat
@socketio.on('message')
def handle_message(message):
    print(f"Mensagem recebida: {message}")
    # Envia a mensagem de volta para todos os clientes conectados
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
