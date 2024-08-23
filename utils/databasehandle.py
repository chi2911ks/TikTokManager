import sqlite3
def addColumn(cursor, query):
    try:cursor.execute(query)
    except: return

class DataBaseHandleTikTok:
    @staticmethod
    def getTypeTiktok():
        conn = sqlite3.connect('data\\data.db')
        cursor = conn.cursor()
        statement = '''SELECT DISTINCT type FROM accounts;'''

        cursor.execute(statement)


        output = cursor.fetchall()
        types = []
        for o in output:
            if o[0]: types.append(o[0])
        return types
    @staticmethod
    def setType(before_value, after_value):
        conn = sqlite3.connect('data\\data.db')
        cursor = conn.cursor()
        update_query = "UPDATE accounts SET type = ? WHERE type = ?"
        cursor.execute(update_query, (after_value, before_value))
        conn.commit()
        cursor.close()
        conn.close()
    @staticmethod
    def getTableAccounts(type=None):
        conn = sqlite3.connect('data\\data.db')
        cursor = conn.cursor()
        if type:
            statement = "SELECT username, password, mail, passmail, cookie, note, description, type FROM accounts WHERE type = '%s'"%type
        else:
            statement = '''SELECT username, password, mail, passmail, cookie, note, description, type FROM accounts'''
        print(statement)
        cursor.execute(statement)


        output = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return output
        # for row in output:
        #     # print(row)
        #     username, password, mail, passmail, cookie, note, description = row
    @staticmethod
    def createDatabase():
        conn = sqlite3.connect('data\\data.db')
        cursor = conn.cursor()
        sql_create_accounts_table = """ CREATE TABLE IF NOT EXISTS accounts (
                                        username text PRIMARY KEY,
                                        password text NOT NULL,
                                        mail text,
                                        passmail text,
                                        cookie text,
                                        note text,
                                        description text,
                                        type text
                                    ); """
       
        cursor.execute(sql_create_accounts_table)
        #dùng cái này do bản cũ vẫn có data, còn bản mới đổi coum table rồi
        addColumn(cursor, "ALTER TABLE accounts ADD COLUMN mail text")
        addColumn(cursor, "ALTER TABLE accounts ADD COLUMN passmail text")
        addColumn(cursor, "ALTER TABLE accounts ADD COLUMN type text")
        conn.commit()
        cursor.close()
        conn.close()
    @staticmethod
    def deleteRow(usernames):
        conn = sqlite3.connect('data\\data.db')
        cursor = conn.cursor()
        record_users_to_delete = usernames
        placeholders = ",".join("?" * len(record_users_to_delete))
        delete_query = f"DELETE FROM accounts WHERE username IN ({placeholders})"
        cursor.execute(delete_query, tuple(record_users_to_delete))
        conn.commit()
        cursor.close()
        conn.close()
    @staticmethod
    def updateRow(username, column, value):
        conn = sqlite3.connect('data\\data.db')
        cursor = conn.cursor()
        update_query = "UPDATE accounts SET %s = ? WHERE username = ?"%column
        cursor.execute(update_query, (value, username))
        conn.commit()
        cursor.close()
        conn.close()
    @staticmethod
    def updateRows(values, username):
        """values: [username, password, mail, passmail, cookie, note, description]"""
        try:
            conn = sqlite3.connect('data\\data.db')
            cursor = conn.cursor()
            usernameOld = values.pop(0)
            
            values.insert(0, username)
            values.append(usernameOld)
            # username, password, mail, passmail, cookie, note, description
            update_query = "UPDATE accounts SET username = ?, password = ?, mail = ?, passmail = ?, cookie = ?, note = ?, description = ? WHERE username = ?"
            # print(tuple(values))
            cursor.execute(update_query, tuple(values))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e: 
            print(e)
            return False
