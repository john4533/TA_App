from project_app.models import Users

def login(name, password):
    noSuchUser = False
    badPassword = False
    try:
        m = Users.objects.get(name)
        badPassword = (m.password != password)
    except:
        noSuchUser = True
    if noSuchUser or badPassword:
        return False
    else:
        return True



    # create courses Bryce
    # create labs Charlie

    # create accounts Anton
    # delete accounts Mohammed

    #User to be deleted cannot be null
    #User is an object
    #return True or false if the account is deleted
    def deleteaccount(User):
        pass



