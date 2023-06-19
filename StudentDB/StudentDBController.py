from StudentDB.StudentDB import StudentDB

class StudentDBController(StudentDB):

    def __init__(self):
        self.studentDB = StudentDB()

    def insertLockerNum(self, lockernum):
        self.studentDB.setLockernum(lockernum)

    def deleteLockerNum(self, lockernum = ''):
        self.studentDB.setLockernum(lockernum)

    def isApply():
        if self.studentDB.lockernum == '':
            return False
        else:
            return True