from LockerDB.LockerDB import LockerDB
from StudentDB.StudentDB import StudentDB

class AdminDBController(StudentDB, LockerDB):
    def __init__(self):
        self.studentDB = StudentDB()
        self.lockerDB = LockerDB()
    
    def setStudentToLocker(self, studentName, lockernum):
        self.studentDB.setLockernum(lockernum)
        self.lockerDB.setStudentName(studentName)
    
    def delStudentToLocker(self):
        self.studentDB.setLockernum("")
        self.lockerDB.setStudentName("")
    
    def getStudentDB(self):
        return self.studentDB.getName()
    
    def getLockerDB(self):
        return self.lockerDB.getLockernum()