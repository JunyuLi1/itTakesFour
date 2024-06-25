from flask import Flask, render_template
from message_style import Message
from config import User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat')
def chat():
    return "chat"

if __name__ == '__main__':
    user = User('168.235.86.101','VC1', 'VC')
    app.run(debug=True)
