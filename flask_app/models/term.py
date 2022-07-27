from config.mysqlconnection import connectToMySQL
import urllib
API_KEY = "562895d5-7b5a-494a-81ec-5743c8220523"
# from libretranslatepy import LibreTranslateAPI


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
        return True

    @classmethod
    def validate_inputs(cls, data):
        return True

