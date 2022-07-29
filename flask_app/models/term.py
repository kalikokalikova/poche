from config.mysqlconnection import connectToMySQL
from flask import flash



class Term:
    def __init__(self, data):
        self.id = data['id']
        self.users_id = data['users_id']
        self.en = data['en']
        self.fr = data['fr']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        print(data)
        query = "insert into terms (users_id, en, fr, notes) values ( %(user_id)s, %(en)s, %(fr)s, %(notes)s );"
        return connectToMySQL('poche_schema').query_db(query, data)

    @classmethod
    def get_all(cls, data):
        query = "select * from terms where users_id = %(id)s;"
        return connectToMySQL('poche_schema').query_db(query, data)

    @classmethod
    def get_term_by_id(cls, data):
        query = "select * from terms where id = %(id)s;"
        result =  connectToMySQL('poche_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_term(cls, data):
        query = "update terms set notes=%(notes)s where id=%(id)s;"
        return connectToMySQL('poche_schema').query_db(query, data)

    @classmethod
    def get_fr_terms_to_browse(cls, data):
        query = "SELECT * FROM poche_schema.terms where users_id = %(id)s order by fr asc;"
        # returns records in alphabetical order by french words
        result = connectToMySQL('poche_schema').query_db(query, data)

        if len(result) > 0:
            terms_to_display = [] # Will return a list of nested dictionaries
            counter = "" # to keep track of what letter we're on
            for r in result: # loop through terms returned from db
                if r['fr'][0].lower() == counter: # if this term starts with the letter we're currently on (the dictionary keyed with that letter already exists)
                    # on the last item in the list, under the key(current letter), the nested key(current term) is assigned value of Term object
                    terms_to_display[-1][counter][r['fr'].lower()] = cls(r)
                else: # The is the first word with a new letter
                    # create key of new letter, assign it the value of dictionary where key is term and value is Term object
                    terms_to_display.append( { r['fr'][0].lower(): { r['fr']: cls(r) } })
                    # update the counter to the new letter
                    counter = r['fr'][0].lower()

            return terms_to_display


    @staticmethod
    def validate_inputs(data):
        # checking that both strings are not empty
        #TODO flash messaging
        return data['en'] and data['fr']

