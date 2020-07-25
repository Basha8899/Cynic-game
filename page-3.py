# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):
    def setupUi(self, Dialog, userObject):
        self.userObject = userObject
        Dialog.setObjectName("Dialog")
        Dialog.resize(685, 762)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, -10, 691, 91))
        self.graphicsView.setStyleSheet("background-color: rgb(0, 0, 74);\n"
"background-color: rgb(8, 8, 118);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 30, 211, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 80, 201, 51))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 180, 421, 111))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(50, 280, 241, 51))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(380, 290, 251, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 55, 101))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(280, 250, 55, 101))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(370, 250, 55, 101))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(630, 250, 55, 101))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(320, 250, 55, 101))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 340, 401, 61))
        self.label_4.setObjectName("label_4")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(40, 630, 611, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(320, 620, 91, 51))
        self.label_10.setObjectName("label_10")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(410, 680, 91, 31))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(180, 670, 241, 51))
        self.label_11.setObjectName("label_11")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 80, 691, 681))
        self.graphicsView_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(75, 401, 531, 211))
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.listWidget.setStyleSheet("background-color: rgb(225, 212, 255);\n"
"color: rgb(7, 7, 7);")
        self.listWidget.setObjectName("listWidget")
        #socket programming        
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(190, 130, 301, 51))
        self.label_12.setObjectName("label_12")
        self.graphicsView_2.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_4.raise_()
        self.line_3.raise_()
        self.label_10.raise_()
        self.lcdNumber.raise_()
        self.label_11.raise_()
        self.listWidget.raise_()
        self.label_12.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        import socket
        self.userObject.ipAddress = socket.gethostname()

        import pymongo as pm
        client = pm.MongoClient('localhost', 27017)
        db = client['psych']
        tempTable = db[self.userObject.gameCode]
        tempTable.insert({'ip':self.userObject.ipAddress,'playerName':self.userObject.userName,'points':0,'answer':"null"})
        entries = []
        for i in tempTable.find():
            entries.append(i['playerName'])        

        self.listWidget.addItems(entries)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">YOUR GAME</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">SECRET CODE : </span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">NOW YOU\'RE IN CHARGE! TELL YOUR</span></p><p align=\"center\"><span style=\" font-size:11pt;\">FRIENDS TO ENTER THIS CODE TO JOIN</span></p><p align=\"center\"><span style=\" font-size:11pt;\">THE GAME</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; color:#787878;\">♦</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; color:#787878;\">♦</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; color:#787878;\">♦</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; color:#787878;\">♦</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt; color:#787878;\">♦</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">WAITING FOR PEOPLE TO JOIN...</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#8a8a8a;\">♦</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">GAME STARTS IN : </span></p></body></html>"))
        ###TEKE CODE FROM DATA BASE
        tempCode = self.userObject.gameCode

        if self.userObject.server == True:
            import pymongo as pm
            client = pm.MongoClient('localhost', 27017)
            db = client['psych']
            code = db['codes']
            checkCode = db['hostCodes']
            from random import randint
            while(True):
                randNo = randint(0, 100)
                temp = code.find().limit(-1).skip(randNo).next()
                tempCode = temp['code']
                if( str(checkCode.find_one({'code':tempCode})) == "None" ):
                    checkCode.insert({'ip':self.userObject.ipAddress, 'code':tempCode, 'deckName':self.userObject.deckName})
                    break
    
        self.userObject.gameCode = tempCode
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#144888;\">"+self.userObject.gameCode+"</span></p></body></html>"))

#
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Dialog = QtWidgets.QDialog()
#    ui = Ui_Dialog3()
#    ui.setupUi(Dialog)
#    Dialog.show()
#    sys.exit(app.exec_())

