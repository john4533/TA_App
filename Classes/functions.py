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

# create labs: Charlie
# ***
# Notice how this can be created into a class quite possibly in the future?
# This is the way we are trying to develop out app from the top down, instead of bottom up
# ***
def createLab(labId, labName):
    pass

def setLabId(labId, labIdOriginal):
    pass

def setLabName(labName, labId):
    pass

def setLabSchedule(schedule, labId):
    pass

def setLabTA(ta, labId):
    pass

    # create accounts Anton
    # delete accounts Mohammed

