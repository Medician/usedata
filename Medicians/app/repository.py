from models.login_details import Login
import db_provider as provider

from sqlite3 import DatabaseError

def create_cust(email, phone, address):
    try:
        query = 'insert into Manya(email, phone, address) values (?, ?, ?)'
        provider.insert_item(query, email, phone, address)
        login = Login(email, phone, address)
        return login


    except DatabaseError as error:
        raise Exception('system error', error)


def get_cust(email):
    user = provider.get_item(email)
    return user


