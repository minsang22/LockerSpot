class StudentDB:

    def __init__(self):
        self.id = ''
        self.password = ''
        self.name = ''
        self.apply = False
        self.lockernum = ''

    def getID(self):
        return self.id
    
    def getPassword(self):
        return self.password
    
    def getName(self):
        return self.name
    
    def getLockernum(self):
        return self.lockernum
    
    def setID(self, id):
        self.id = id
    
    def setPassword(self, password):
        self.password = password
    
    def setName(self, name):
        self.name = name
    
    def setLockernum(self, lockernum):
        self.lockernum = lockernum

    