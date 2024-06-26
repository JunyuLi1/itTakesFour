from flask import Flask, render_template
from chat.message_style import Message
from config import User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/chat')
def chat():
    result = user.contactobj.retrieve_all()
    contacts = []
    for item in result:
        if item.recipient not in contacts:
            contacts.append(item.recipient)
    return render_template('chat.html', contacts=contacts)

if __name__ == '__main__':
    user = User('168.235.86.101','VC1', 'VC')
    app.run(debug=True)
