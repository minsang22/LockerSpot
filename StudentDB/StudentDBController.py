from StudentDB.StudentDB import StudentDB

class StudentDBController(StudentDB):

    def __init__(self):
        self.studentDB = StudentDB()

    def insertLockerNum(self, lockernum):
        self.studentDB.setLockernum(lockernum)

    def deleteLockerNum(self, lockernum = ''):
        self.studentDB.setLockernum(lockernum)

    def isApply(self, apply = False):
        if self.studentDB.lockernum == '':
            return apply
        else:
            return True