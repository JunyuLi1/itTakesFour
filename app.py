from flask import Flask, render_template, request
from config import User
from database import verify_login_status

app = Flask(__name__)
user = None

@app.route('/')
def home():
    return render_template('home.html', status='login')

@app.route('/login', methods=['GET','POST'])
def login():
    #login function, store in global var user
    global user
    if request.method == 'POST':
        print(request.form)
        name = request.form['username']
        pwd = request.form['password']
        result = verify_login_status(name, pwd)
        if result is not None:
            user = User('168.235.86.101', name, pwd)
            return render_template('home.html', status='logout')
        else:
            return render_template('login.html', status='No such user!')
    else:
        return render_template('login.html')

@app.route('/chat',methods=['GET','POST'])
def chat():
    #TODO: 自动刷新获取最新消息
    global user
    if user is None:
        return render_template('login.html')
    else:
        contacts = user.get_all_contacts()
        if request.method == 'POST':
            print(request.form)
            person = request.form['chat_friend']
            if person not in contacts:
                contacts.append(person)
                user.add_new_contact(contacts)
            history = user.load_contact_history(person)
            if 'send_message' in request.form:
                message_input = request.form['send_message']
                user.store_send_history(person, message_input)
                user.contactobj.send(message_input,person)
            return render_template('chat.html', contacts=contacts, history=history,selected_radio=person)
        else:
            return render_template('chat.html', contacts=contacts)


if __name__ == '__main__':
    #user = User('168.235.86.101','VC1', 'VC') #config user, could change later
    #user = User('168.235.86.101','sbHammer', 'sbHammer') #config user, could change later
    app.run(debug=True)
