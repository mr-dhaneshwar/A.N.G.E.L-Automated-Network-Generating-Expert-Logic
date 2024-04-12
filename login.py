import sqlite3


def connect():
    global cursor, con
    try:
        con = sqlite3.connect('ANGEL.db')
        print('connected to server')
        cursor = con.cursor()
        return True
    except sqlite3.Error as e:
        print(e, 'not connnected to server')
        return False


def crclose():
    cursor.close()
    con.close()
    print('connection closed')


def createTable():
    if not connect():
        return 'not connect'
    query = '''create table USER(username varchar(20) primary key,password varchar(20), name varchar(20), dob varchar(10))'''
    try:
        cursor.execute(query)
        print('table created succesfully')
        return True
    except sqlite3.Error as e:
        e = str(e)
        if 'already exists' in e:
            return True
        print(e)


def drop_table():
    if not connect():
        return 'not connect'
    sql = "DROP TABLE USER"

    # execute the SQL statement
    cursor.execute(sql)
    print('table deleted')

    # commit the changes to the database
    con.commit()
    crclose()


def singup(use, pas, name, dob):
    if createTable() == 'not connect':
        return 'not connect'
    try:
        query = '''select * from USER where username=?'''
        info = (use,)
        cursor.execute(query, info)
        data = cursor.fetchone()
        if not data:
            query = '''insert into USER values(?,?,?,?)'''
            info = (use, pas, name, dob)
            cursor.execute(query, info)
            con.commit()
            print('Account created succesfully')
            return 1
        else:
            print('User already exist')
            return 2

    except sqlite3.Error as e:
        print(e, 'singup')


def singin(use, pas):
    if createTable() == 'not connect':
        return 'not connect'
    try:
        query = '''select * from USER where username=? or password = ?'''
        info = (use, pas)
        cursor.execute(query, info)
        data = cursor.fetchone()
        if data and info[0] == data[0]:
            if data[1] == info[1]:
                print('login succesfull')
                crclose()
                return 1
            else:
                print('invalid password')
                crclose()
                return 2
        else:
            print("Username not found please Sing Up")
            crclose()
            return 3
    except sqlite3.Error as e:
        print(e, 'singin')


def forgot(use, dob, new=''):
    if createTable() == 'not connect':
        return 'not connect'

    try:
        query = '''select * from USER where username=? or dob=?'''
        info = (use, dob)
        cursor.execute(query, info)
        data = cursor.fetchone()

        if data and info[0] == data[0]:
            if data[3] == info[1]:
                query = '''UPDATE USER SET password = ? WHERE username=?'''
                info = (new, use)
                cursor.execute(query, info)
                con.commit()
                print('password changed succesfully...')
                crclose()
                return 1

            else:
                print('invalid credentials')
                crclose()
                return 2

        else:
            print("Username not found please Sing Up")
            crclose()
            return 3

    except sqlite3.Error as e:
        print(e, 'forgot')
