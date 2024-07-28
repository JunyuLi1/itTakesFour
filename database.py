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

def get_chat_history(username, friendname, offset=0):
    try:
        with sqlite3.connect('./user/userdata.db') as data_connect:
            #data_connect.execute("PRAGMA foreign_keys = ON;")
            impl_format = f"""SELECT 'receive' AS message_type, sender, time, content
                            FROM {username}_receive
                            WHERE sender = ?

                            UNION ALL

                            SELECT 'send' AS message_type, receiver, time, content
                            FROM {username}_send
                            WHERE receiver = ?

                            ORDER BY time DESC
                            LIMIT 50 OFFSET {offset};"""

            all_chat_his  = data_connect.execute(impl_format, (friendname, friendname))
            return all_chat_his.fetchall() #('testSendFromF', '2')
    except Exception as error:
        return str(error)

def store_chat_history(chat_type, username, friendname, time, content):
    try:
        with sqlite3.connect('./user/userdata.db') as data_connect:
            #data_connect.execute("PRAGMA foreign_keys = ON;")
            if chat_type == 'receive':
                command = f'''INSERT INTO {username}_receive (sender, time, content) VALUES (?, ?, ?);'''
                data_connect.execute(command, (friendname, time, content))
            if chat_type == 'send':
                command = f'''INSERT INTO {username}_send (receiver, time, content) VALUES (?, ?, ?);'''
                data_connect.execute(command, (friendname, time, content))
            else:
                raise Exception('chat_type is not defined')
    except Exception as error:
        return str(error)


def get_contacts(username):
    try:
        with sqlite3.connect('./user/userdata.db') as data_connect:
            impl_format = '''SELECT contacts FROM user_reg WHERE username = ?;'''
            user_id  = data_connect.execute(impl_format, (username,))
            result = user_id.fetchone()[0]
            return result
    except Exception as error:
        return str(error)

def update_new_contacts(contacts, username):
    try:
        with sqlite3.connect('./user/userdata.db') as data_connect:
            cursor = data_connect.cursor()
            impl_format = "UPDATE user_reg SET contacts = ? WHERE username = ?;"
            cursor.execute(impl_format, (contacts, username))
            data_connect.commit()
    except Exception as error:
        return str(error)


if __name__ == '__main__':
    #print(verify_login_status('VC', 'VC'))
    #store_chat_history('receive','VC1', 'Frank',time.time(), 'testSend')
    print(get_contacts('VC1'), type(get_contacts('VC1')))
