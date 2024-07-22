import sqlite3

def verify_login_status(username, password):
    try:
        with sqlite3.connect('./user/userdata.db') as data_connect:
            #data_connect.execute("PRAGMA foreign_keys = ON;")
            
            impl_format = '''SELECT id FROM user_reg WHERE username = ? AND password = ?;'''
            user_id  = data_connect.execute(impl_format, (username, password))
            result = user_id.fetchone()
            return result
    except Exception as error:
        return str(error)

def get_chat_history(username, friendname):
    try:
        with sqlite3.connect('./user/userdata.db') as data_connect:
            #data_connect.execute("PRAGMA foreign_keys = ON;")
            #怎么样同时加载用户发的和收到的？
            impl_format = f'''SELECT content, time FROM {username} WHERE sender = ?;'''
            all_chat_his  = data_connect.execute(impl_format, (friendname, ))
            while True:
                chat_his = all_chat_his.fetchone()
                if chat_his is None:
                    break
                yield chat_his #('testSendFromF', '2')
    except Exception as error:
        return str(error)

def store_chat_history(chat_type, username, friendname, time, content):
    try:
        with sqlite3.connect('./user/userdata.db') as data_connect:
            #data_connect.execute("PRAGMA foreign_keys = ON;")
            if chat_type == 'new_info':
                command = f'''INSERT INTO {username} (sender, receiver, time, content) VALUES (?, ?, ?, ?);'''
                data_connect.execute(command, (friendname, username, time, content))
            else:
                command = f'''INSERT INTO {username} (sender, receiver, time, content) VALUES (?, ?, ?, ?);'''
                data_connect.execute(command, (username, friendname, time, content))
            
    except Exception as error:
        return str(error)

if __name__ == '__main__':
    #print(verify_login_status('VC', 'VC'))
    print(next(get_chat_history('VC1', 'Frank')))