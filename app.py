from flask import Flask, render_template, request
from chat.message_style import Message
from config import User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/chat',methods=['GET','POST'])
def chat():
    result = user.contactobj.retrieve_all()
    contacts = {}
    for item in result:
        if item.recipient not in contacts:
            contacts[item.recipient] = []
            contacts[item.recipient].append(item.message)
        else:
            contacts[item.recipient].append(item.message)
    if request.method == 'POST':
        #message_input = request.form['send_message']
        print(request.form)
        #勾选问题或发送和选择问题
        person = request.form['chat_friend']
        if 'send_message' in request.form:
            message_input = request.form['send_message']
        if person not in contacts.keys():
            contacts[person] = []
        return render_template('chat.html', contacts=contacts.keys(), history=contacts[person],selected_radio=person)
    else:
        return render_template('chat.html', contacts=contacts.keys())

if __name__ == '__main__':
    user = User('168.235.86.101','VC1', 'VC')
    app.run(debug=True)
