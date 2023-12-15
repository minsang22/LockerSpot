import sys
import requests
import json
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from LockerDB.LockerDBController import LockerDBController
from StudentDB.StudentDBController import StudentDBController
from AdminDB.AdminDBController import AdminDBController

login_ui = uic.loadUiType("UI/LoginWindow.ui")[0]
register_ui = uic.loadUiType("UI/RegisterWindow.ui")[0]
apply_ui = uic.loadUiType("UI/ApplyWindow.ui")[0]
return_ui = uic.loadUiType("UI/ReturnWindow.ui")[0]
admin_ui = uic.loadUiType("UI/AdminWindow.ui")[0]

class LoginWindow(QMainWindow, login_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registerBtn.clicked.connect(self.Register)
        self.loginBtn.clicked.connect(self.Login)
        self.loginBtn_2.clicked.connect(self.adminLogin)
    
    def Register(self):
        loginwindow.hide()
        registerwindow.show()
        
    def Login(self):
        server_addr = "http://10.223.113.129:8000"
        data = {"student_id" : self.id_edit.text(),
                "password" : self.pw_edit.text(),  "path": "/student/signin"}
        res = requests.post(server_addr,json = data,
                            headers={"accept": "application/json",
                                     "Content-Type": "application/json"})
        if res.json()["status"] :
            loginwindow.hide()
            applywindow.show()
        else : 
            self.loginBtn.setText("등록되지 않은 계정")
            # check-point : setText가 아닌 새 윈도우를 띄워주는 형식으로 수정

    def adminLogin(self):
        labelid = self.id_edit.text()
        labelpassword = self.pw_edit.text()
        userid, userpassword = self.read_studentDB()
        if userid == labelid and userpassword == labelpassword :
            loginwindow.hide()
            adminwindow.show()
        else : 
            self.loginBtn.setText("등록되지 않은 계정")
            # check-point : setText가 아닌 새 윈도우를 띄워주는 형식으로 수정

class RegisterWindow(QMainWindow, register_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registerBtn.clicked.connect(self.register)
        self.sdc = StudentDBController()

    def write_studentDB(self):
        server_addr = "http://10.223.113.129:8000"
        data = {"student_id" : self.sdc.getID(), "password" : self.sdc.getPassword(), "name" : self.sdc.getName(),  "path": "/student/signup"}
        res = requests.post(server_addr, json = data, headers={
        "accept": "application/json",
        "Content-Type": "application/json",})
        
    def register(self):
        self.sdc.setID(self.id_edit.text())
        self.sdc.setPassword(self.pw_edit.text())
        self.sdc.setName(self.name_edit.text())
        self.sdc.isApply()
        self.sdc.setLockernum("")
        self.write_studentDB()
        registerwindow.hide()
        loginwindow.show()        
class ApplyWindow(QMainWindow, apply_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectlocker = ""
        self.sdc = StudentDBController()
        server_addr = "http://10.223.113.129:8000"
        data = {"path": "/locker/return_locker"}
        res = requests.post(server_addr, json=data,
                            headers={"accept": "application/json",
                                     "Content-Type": "application/json"})
        if res.json()["A-1"]:
            self.lockerspace1.setText("사용중")
        if res.json()["A-2"]:
            self.lockerspace2.setText("사용중")
        if res.json()["A-3"]:
            self.lockerspace3.setText("사용중")
        if res.json()["A-4"]:
            self.lockerspace4.setText("사용중")
        if res.json()["A-5"]:
            self.lockerspace5.setText("사용중")
        if res.json()["B-1"]:
            self.lockerspace6.setText("사용중")
        if res.json()["B-2"]:
            self.lockerspace7.setText("사용중")
        if res.json()["B-3"]:
            self.lockerspace8.setText("사용중")
        if res.json()["B-4"]:
            self.lockerspace9.setText("사용중")
        if res.json()["B-5"]:
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

    def lockerspace1btn(self):
        if self.lockerspace1.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace1.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "1"
            
    def lockerspace2btn(self):
        if self.lockerspace2.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace2.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "2"
            
    def lockerspace3btn(self):
        if self.lockerspace3.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace3.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "3"
            
    def lockerspace4btn(self):
        if self.lockerspace4.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace4.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "4"
            
    def lockerspace5btn(self):
        if self.lockerspace5.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace5.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "5"
            
    def lockerspace6btn(self):
        if self.lockerspace6.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace6.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "6"
            
    def lockerspace7btn(self):
        if self.lockerspace7.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace7.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "7"
            
    def lockerspace8btn(self):
        if self.lockerspace8.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace8.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "8"
            
    def lockerspace9btn(self):
        if self.lockerspace9.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace9.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "9"
            
    def lockerspace10btn(self):
        if self.lockerspace10.text() == "사용중" :
            self.name_label.setText("학생 이름 : 성정규")
            self.locker_label.setText("선택한 사물함 : 사용중인 사물함")
            
        else : 
            self.name_label.setText("학생 이름 : 성정규")
            lockernum = self.lockerspace10.text()
            self.locker_label.setText("선택한 사물함 : " + lockernum)
            self.selectlocker = "10"
            
    def apply(self):
        if self.selectlocker == "1" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id" : "A-1", "path": "/locker/apply"}
            requests.post(server_addr, json=data,headers={"accept": "application/json","Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : A-1 ")
            returnwindow.lockernum = "1"

        elif self.selectlocker == "2" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "A-2", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : A-2 ")
            returnwindow.lockernum = "2"

        elif self.selectlocker == "3" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "A-3", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : A-3 ")
            returnwindow.lockernum = "3"

        elif self.selectlocker == "4" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "A-4", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : A-4 ")
            returnwindow.lockernum = "4"

        elif self.selectlocker == "5" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "A-5", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : A-5 ")
            returnwindow.lockernum = "5"

        elif self.selectlocker == "6" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "B-1", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : B-1 ")
            returnwindow.lockernum = "6"

        elif self.selectlocker == "7" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "B-2", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : B-2 ")
            returnwindow.lockernum = "7"

        elif self.selectlocker == "8" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "B-3", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : B-3 ")
            returnwindow.lockernum = "8"

        elif self.selectlocker == "9" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "B-4", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : B-4 ")
            returnwindow.lockernum = "9"

        elif self.selectlocker == "10" :
            server_addr = "http://10.223.113.129:8000"
            data = {"locker_id": "B-5", "path": "/locker/apply"}
            requests.post(server_addr, json=data,
                          headers={"accept": "application/json", "Content-Type": "application/json"})
            returnwindow.locker_label.setText("대여중인 사물함 : B-5 ")
            returnwindow.lockernum = "10"
        
        applywindow.hide()
        returnwindow.show()
        
class ReturnWindow(QMainWindow, return_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name_label.setText("학생 이름 : " + self.read_studentname())
        self.returnBtn.clicked.connect(self.returnlocker)
        self.sdc = StudentDBController()
        self.lockernum = ""
        self.usageHistoryBtn.clicked.connect(self.usageHistory)
        
    def read_studentname(self):
        with open("StudentDB/StudentID.txt", "r") as file :
            lines = file.readlines()
            name = lines[2].strip()
            return name
    
    def returnlocker(self) :
        with open("LockerDB/LockerList.txt", "r") as fr :
            lines = fr.readlines()
            if self.lockernum == "10" :
                lines[int(self.lockernum)-1] = "0"
            else :
                lines[int(self.lockernum)-1] = "0\n"
            fr.close()
            
        with open("LockerDB/LockerList.txt", "w") as fw :
            for line in lines :
                fw.write(line)
            fw.close()
        returnwindow.hide()
        applywindow.show()
        
    def usageHistory(self):
        self.usageHistoryList.insertItem(0, "A-1")
        
        
        
    
class AdminWindow(QMainWindow, admin_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.translate_locknum = ""
        #QComboBox 추가
        self.student_combo_box.addItem("윤민상")
        self.student_combo_box.addItem("성정규")
        self.student_combo_box.addItem("안수현")
        self.sdc = StudentDBController()
        self.ldc = LockerDBController()
        self.adc = AdminDBController()
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
        
        self.returnBtn.clicked.connect(self.returnlocker)
        self.setStudentToLockerBtn.clicked.connect(self.assignstudent)
        self.getStudentDBBtn.clicked.connect(self.getStudentDB)
        self.student_list.itemClicked.connect(self.studentListClicked)
        
    def rebtntext(self):
        with open("LockerDB/LockerList.txt", "r") as file :
            lines = file.readlines()
            if int(lines[0]) == 0 :
                self.lockerspace1.setText("A-1")
            if int(lines[1]) == 0 :
                self.lockerspace2.setText("A-2")
            if int(lines[2]) == 0 :
                self.lockerspace3.setText("A-3")
            if int(lines[3]) == 0 :
                self.lockerspace4.setText("A-4")
            if int(lines[4]) == 0 :
                self.lockerspace5.setText("A-5")
            if int(lines[5]) == 0 :
                self.lockerspace6.setText("B-1")
            if int(lines[6]) == 0 :
                self.lockerspace7.setText("B-2")
            if int(lines[7]) == 0 :
                self.lockerspace8.setText("B-3")
            if int(lines[8]) == 0 :
                self.lockerspace9.setText("B-4")
            if int(lines[9]) == 0 :
                self.lockerspace10.setText("B-5")   
    
    def rebtntext2(self):
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

    def read_studentname(self):
        with open("StudentDB/StudentID.txt", "r") as file :
            lines = file.readlines()
            name = lines[2].strip()
            return name
    
    def lockerspace1btn(self):
        if self.lockerspace1.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : A-1")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "1"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : A-1")
            self.translate_locknum = "1"
            
    def lockerspace2btn(self):
        if self.lockerspace2.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : A-2")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "2"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : A-2")
            self.translate_locknum = "2"
            
    def lockerspace3btn(self):
        if self.lockerspace3.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : A-3")
            self.return_student.setText("사용중인 학생 : 안수현")
            self.translate_locknum = "3"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : A-3")
            self.translate_locknum = "3"
            
    def lockerspace4btn(self):
        if self.lockerspace4.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : A-4")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "4"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : A-4")
            self.translate_locknum = "4"
            
    def lockerspace5btn(self):
        if self.lockerspace5.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : A-5")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "5"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : A-5")
            self.translate_locknum = "5"
            
    def lockerspace6btn(self):
        if self.lockerspace6.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : B-1")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "6"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : B-1")
            self.translate_locknum = "6"
    
    def lockerspace7btn(self):
        if self.lockerspace7.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : B-2")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "7"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : B-2")
            self.translate_locknum = "7"
    
    def lockerspace8btn(self):
        if self.lockerspace8.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : B-3")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "8"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : B-3")
            self.translate_locknum = "8"
            
    def lockerspace9btn(self):
        if self.lockerspace9.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : B-4")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "9"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : B-4")
            self.translate_locknum = "9"
            
    def lockerspace10btn(self):
        if self.lockerspace10.text() == "사용중" :
            self.return_locker.setText("선택한 사물함 : B-5")
            self.return_student.setText("사용중인 학생 : " + self.read_studentname())
            self.translate_locknum = "10"
            
        else : 
            self.assign_locker.setText("선택한 사물함 : B-5")
            self.translate_locknum = "10"
            
    
    def returnlocker(self):
        with open("LockerDB/LockerList.txt", "r") as fr :
            lines = fr.readlines()
            if self.translate_locknum == "10" :
                lines[int(self.translate_locknum)-1] = "0"
            else :
                lines[int(self.translate_locknum)-1] = "0\n"
            fr.close()
            
        with open("LockerDB/LockerList.txt", "w") as fw :
            for line in lines :
                fw.write(line)
            fw.close()
        self.rebtntext()
        
    def assignstudent(self):
        with open("LockerDB/LockerList.txt", "r") as fr :
            lines = fr.readlines()
            if self.translate_locknum == "10" :
                lines[int(self.translate_locknum)-1] = "1"
            else :
                lines[int(self.translate_locknum)-1] = "1\n"
            fr.close()
            
        with open("LockerDB/LockerList.txt", "w") as fw :
            for line in lines :
                fw.write(line)
            fw.close()
        self.rebtntext2()
        
    def getStudentDB(self):
        self.student_list.insertItem(0, "윤민상")
        self.student_list.insertItem(1, "성정규")
        self.student_list.insertItem(2, "안수현")
        
    def studentListClicked(self):
        if self.student_list.currentRow() == 0 :
            self.student_name.setText("이름 : 윤민상")
            self.check_usage.setText("사용 여부 : 사용중")
            self.usage_locker.setText("사용중인 사물함 : A-1")
        
        elif self.student_list.currentRow() == 1 :
            self.student_name.setText("이름 : 성정규")
            self.check_usage.setText("사용 여부 : 사용중")
            self.usage_locker.setText("사용중인 사물함 : A-2")
        
        elif self.student_list.currentRow() == 2 :
            self.student_name.setText("이름 : 안수현")
            self.check_usage.setText("사용 여부 : 사용중이 아님")
            self.usage_locker.setText("사용중인 사물함 : 없음")
                    
        
                
            
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    loginwindow = LoginWindow()
    registerwindow = RegisterWindow()
    applywindow = ApplyWindow()
    returnwindow = ReturnWindow()
    adminwindow = AdminWindow()
    loginwindow.show()
    app.exec_()

