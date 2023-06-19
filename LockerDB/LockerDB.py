class LockerDB:

    def __init__(self):
        self.lockernum = ""
        self.using = False
        self.studentName = ""
    
    def getLockernum(self):
        return self.lockernum
    
    def getUsing(self):
        return self.using
    
    def getStudentName(self):
        return self.studentName
    
    def setLockernum(self, lockernum):
        self.lockernum = lockernum
    
    def setUsing(self, using):
        self.using = using
        
    def setStudentName(self, studentName):
        self.studentName = studentName