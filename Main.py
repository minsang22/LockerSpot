import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from LockerDB.LockerDBController import LoackerDBController
#from Manager.ManagerController import ManagerController

login_ui = uic.loadUiType("UI/LoginWindow.ui")[0]
apply_ui = uic.loadUiType("UI/ApplyWindow.ui")[0]
return_ui = uic.loadUiType("UI/ReturnWindow.ui")[0]
admin_ui = uic.loadUiType("UI/AdminWindow.ui")[0]

class LoginWindow(QMainWindow, login_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginBtn.clicked.connect(self.Login)
        
    def read_studentDB(self):
        with open("StudentDB/StudentID.txt", "r") as file :
            lines = file.readlines()
            id = lines[0].strip()
            password = lines[1].strip()
            name = lines[2].strip()
            return id, password
        
    def Login(self):
        labelid = self.id_edit.text()
        labelpassword = self.pw_edit.text()
        userid, userpassword = self.read_studentDB()
        if userid == labelid and userpassword == labelpassword :
            loginwindow.hide()
            applywindow.show()
        else : 
            self.loginBtn.setText("등록되지 않은 계정")
            # check-point : setText가 아닌 새 윈도우를 띄워주는 형식으로 수정
        
class ApplyWindow(QMainWindow, apply_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectlocker = ""
        with open("LockerDB/LockerList.txt", "r") as file :
            lines = file.readlines()
            if int(lines[0]) == 1 :
                self.lockerspace1.setText("사용중")
            if int(lines[1]) == 1 :
                self.lockerspace2.setText("사용중")
            if int(lines[2]) == 1 :
                self.lockerspace3.setText("사용중")
            if int(lines[3]) == 1 :
                self.lockerspace4.setText("사용중")
            if int(lines[4]) == 1 :
                self.lockerspace5.setText("사용중")
            if int(lines[5]) == 1 :
                self.lockerspace6.setText("사용중")
            if int(lines[6]) == 1 :
                self.lockerspace7.setText("사용중")
            if int(lines[7]) == 1 :
                self.lockerspace8.setText("사용중")
            if int(lines[8]) == 1 :
                self.lockerspace9.setText("사용중")
            if int(lines[9]) == 1 :
                self.lockerspace10.setText("사용중")
            
        
        self.lockerspace1.clicked.connect(self.lockerspace1btn)
        self.lockerspace2.clicked.connect(self.lockerspace2btn)
        self.lockerspace3.clicked.connect(self.lockerspace3btn)
        self.lockerspace4.clicked.connect(self.lockerspace4btn)
        self.lockerspace5.clicked.connect(self.lockerspace5btn)
        self.lockerspace6.clicked.connect(self.lockerspace6btn)
        self.lockerspace7.clicked.connect(self.lockerspace7btn)
        self.lockerspace8.clicked.connect(self.lockerspace8btn)
        self.lockerspace9.clicked.connect(self.lockerspace9btn)
        self.lockerspace10.clicked.connect(self.lockerspace10btn)
        
        self.applyBtn.clicked.connect(self.apply)
        
    def read_studentname(self):
        with open("StudentDB/StudentID.txt", "r") as file :
            lines = file.readlines()
            name = lines[2].strip()
            return name
    
    def lockerspace1btn(self):
        if self.lockerspace1.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace1.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "1"
            
    def lockerspace2btn(self):
        if self.lockerspace2.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace2.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "2"
            
    def lockerspace3btn(self):
        if self.lockerspace3.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace3.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "3"
            
    def lockerspace4btn(self):
        if self.lockerspace4.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace4.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "4"
            
    def lockerspace5btn(self):
        if self.lockerspace5.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace5.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "5"
            
    def lockerspace6btn(self):
        if self.lockerspace6.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace6.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "6"
            
    def lockerspace7btn(self):
        if self.lockerspace7.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace7.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "7"
            
    def lockerspace8btn(self):
        if self.lockerspace8.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace8.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "8"
            
    def lockerspace9btn(self):
        if self.lockerspace9.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace9.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "9"
            
    def lockerspace10btn(self):
        if self.lockerspace10.text() == "사용중" :
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : " + self.read_studentname())
            lockernum = self.lockerspace10.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "10"
            
    def apply(self):
        with open("LockerDB/LockerList.txt", "r") as fr :
            lines = fr.readlines()
            if self.selectlocker == "10" :
                lines[int(self.selectlocker)-1] = "1"
            else :
                lines[int(self.selectlocker)-1] = "1\n"
            fr.close()
            
        with open("LockerDB/LockerList.txt", "w") as fw :
            for line in lines :
                fw.write(line)
            fw.close()
            
        if self.selectlocker == "1" :
            returnwindow.locker_label.setText("대여중인 사물함 : A-1 ")
        elif self.selectlocker == "2" :
            returnwindow.locker_label.setText("대여중인 사물함 : A-2 ")
        elif self.selectlocker == "3" :
            returnwindow.locker_label.setText("대여중인 사물함 : A-3 ")
        elif self.selectlocker == "4" :
            returnwindow.locker_label.setText("대여중인 사물함 : A-4 ")
        elif self.selectlocker == "5" :
            returnwindow.locker_label.setText("대여중인 사물함 : A-5 ")
        elif self.selectlocker == "6" :
            returnwindow.locker_label.setText("대여중인 사물함 : B-1 ")
        elif self.selectlocker == "7" :
            returnwindow.locker_label.setText("대여중인 사물함 : B-2 ")
        elif self.selectlocker == "8" :
            returnwindow.locker_label.setText("대여중인 사물함 : B-3 ")
        elif self.selectlocker == "9" :
            returnwindow.locker_label.setText("대여중인 사물함 : B-4 ")
        elif self.selectlocker == "10" :
            returnwindow.locker_label.setText("대여중인 사물함 : B-5 ")
        
        applywindow.hide()
        returnwindow.show()
        
class ReturnWindow(QMainWindow, return_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name_label.setText("학생 이름 : " + self.read_studentname())
        
    def read_studentname(self):
        with open("StudentDB/StudentID.txt", "r") as file :
            lines = file.readlines()
            name = lines[2].strip()
            return name
    
    
    
class AdminWindow(QMainWindow, admin_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
            
                
            
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    loginwindow = LoginWindow()
    applywindow = ApplyWindow()
    returnwindow = ReturnWindow()
    adminwindow = AdminWindow()
    loginwindow.show()
    app.exec_()

