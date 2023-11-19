from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.classes.board import Board


app = Flask(__name__)
CORS(app) 

socketio = SocketIO(app)

board = None

@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/site/js/<filename>')
def uploaded_js(filename):
    return send_from_directory('js', filename)

@app.route('/site/css/<filename>')
def uploaded_css(filename):
    return send_from_directory('css', filename)


@socketio.on('message_from_client')
def handle_message(message):
    global board  
    print('Message from client:', message)
    
    if message == 'start':
        board = Board()
        print(board)
        socketio.emit('message_from_server', 'Доска создана')  
    elif message == 'get_new_figures':
        socketio.emit('message_from_server', board.encode())
       

if __name__ == '__main__':
    socketio.run(app, debug=True)
