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
            #user.load_chat_history()
            return render_template('home.html', status='logout')
        else:
            return render_template('login.html', status='No such user!')
    else:
        return render_template('login.html')

@app.route('/chat',methods=['GET','POST'])
def chat():
    #TODO: retrieve new or all
    #TODO: creating new contacts
    #TODO: auto refresh for receving new_message
    #TODO: display all message according time,split in two different parts
    # contact parts = {'SuperHammerB': {'SuperHammerB':[],'user:[]'}}
    #TODO: Impoertant !!! store message in local (new server if applicable)
    global user
    if user is None:
        return render_template('login.html')
    else:
        #如果是新用户需要的检查条件没完成
        contacts = user.get_all_contacts()
        if request.method == 'POST':
            print(request.form)
            person = request.form['chat_friend']
            if person not in contacts: #创建新的contact功能还没完成
                contacts.append(person)
                pass
            history = user.load_contact_history(person)
            print(history)
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
