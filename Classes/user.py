from project_app.models import Users

class User():

    def __init__(self, name="", password="", email="", phone="", address=""):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address

    def create_user(self, name, password, email):
        pass

    def edit_username(self, name):
        pass

    def edit_password(self, password):
        pass

    def edit_email(self, email):
        pass

    def edit_phone(self, phone):
        pass

    def edit_address(self, address):
        pass

    def delete_user(self, name, email):
        pass

    def send_email(self, email):
        pass

    def login(self, name, password):
        pass