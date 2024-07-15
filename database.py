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


if __name__ == '__main__':
    print(verify_login_status('VC', 'VC'))
