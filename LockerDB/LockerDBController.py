from LockerDB.LockerDB import LockerDB

class LockerDBController(LockerDB):

    def __init__(self):
        self.lockerDB = LockerDB()
    
    def insertStudent(self, studentName):
        self.lockerDB.setStudentName(studentName)

    def deleteStudent(self, studentName = ''):
        self.lockerDB.setLockernum(studentName)

    def isUsing(self, using = False):
        if self.lockerDB.studentName == "":
            return using
        else:
            return True