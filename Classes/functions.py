from project_app.models import *

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

    def create_course(id, name, schedule, instructor, TA, graderstatues, labs):
        try:
            i = Course.objects.get(id)
            return False

        except:
            return True

    # create courses Bryce
    # create labs Charlie

    # create accounts Anton
    # delete accounts Mohammed

