from config.mysqlconnection import connectToMySQL
from flask import flash



class Term:
    def __init__(self, data):
        self.id = data['id']
        self.users_id = data['users_id']
        self.eng = data['eng']
        self.fr = data['fr']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        print(data)
        query = "insert into terms (users_id, en, fr, notes) values ( %(user_id)s, %(en)s, %(fr)s, %(notes)s );"
        return connectToMySQL('poche_schema').query_db(query, data)

    @staticmethod
    def validate_inputs(data):
        # checking that both strings are not empty
        #TODO flash messaging
        return data['en'] and data['fr']

