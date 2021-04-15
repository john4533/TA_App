from project_app.models import Users

class User():

    def __init__(self, name="", password=""):
        self.name = name
        self.password = password

    def create_user(self):
        pass

    def edit_username(self):
        pass

    def edit_password(self):
        pass

    def login(self, name, password):
        pass