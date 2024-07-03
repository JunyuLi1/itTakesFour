from flask import Flask, render_template, request
from chat.message_style import Message
from config import User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Zot_template.html')

@app.route('/chat',methods=['GET','POST'])
def chat():
    #TODO: retrieve new or all
    #TODO: creating new contacts
    #TODO: auto refresh for receving new_message
    #TODO: display all message according time,split in two different parts
    result = user.contactobj.retrieve_all()
    contacts = {}
    for item in result:
        if item.recipient not in contacts:
            contacts[item.recipient] = []
            contacts[item.recipient].append(item.message)
        else:
            contacts[item.recipient].append(item.message)
    if request.method == 'POST':
        print(request.form)
        person = request.form['chat_friend']
        if 'send_message' in request.form:
            message_input = request.form['send_message']
            user.contactobj.send(message_input,person)
        if person not in contacts.keys():
            contacts[person] = []
        return render_template('chat.html', contacts=contacts.keys(), history=contacts[person],selected_radio=person)
    else:
        return render_template('chat.html', contacts=contacts.keys())


if __name__ == '__main__':
    user = User('168.235.86.101','VC1', 'VC') #config user, could change later
    #user = User('168.235.86.101','sbHammer', 'sbHammer') #config user, could change later
    app.run(debug=True)
