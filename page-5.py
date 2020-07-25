# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog5(object):
    def getPickedAns(self):
        selectedAns = self.listWidget.currentItem().text()
        if( len(selectedAns) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("ANS NOT SELECTED")
            error_dialog.exec_()                        
        else:       
            import pymongo as pm        
            client = pm.MongoClient('localhost', 27017)        
            db = client['psych']        
            updateCount = db[self.userObject.gameCode]
            updateCount.update({'answer': selectedAns},{'$inc': {'points': 1}})
            a = updateCount.find_one({'answer': selectedAns})
            self.userObject.pickedans = a['playerName']

    def setupUi(self, Dialog, userObject):
        self.userObject = userObject
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 748)
        Dialog.setStyleSheet("color: rgb(225, 225, 225);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 90, 771, 131))
        self.label.setObjectName("label")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 811, 231))
        self.graphicsView_2.setStyleSheet("background-color: rgb(0, 0, 103);\n"
"color: rgb(255, 255, 255);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 791, 71))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 40, 811, 61))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 40, 55, 51))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 270, 91, 391))
        self.line_2.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(690, 270, 91, 391))
        self.line_3.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(10)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(50, 250, 681, 51))
        self.line_4.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(10)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(40, 640, 701, 51))
        self.line_5.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(10)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 690, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 240, 311, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50, 280, 681, 381))
        self.listWidget.setObjectName("listWidget")
        
        #ansfrom datbase
        import pymongo as pm
        client = pm.MongoClient('localhost', 27017)
        db = client['psych']
        tempTable = db[self.userObject.gameCode]
        entries = []
        
        for i in tempTable.find():
            entries.append(i['answer'])        

        self.listWidget.addItems(entries)
        
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 240, 55, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 240, 55, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(190, 240, 55, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(520, 240, 55, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(550, 240, 55, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(580, 240, 81, 31))
        self.label_10.setObjectName("label_10")
        self.graphicsView_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.listWidget.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.pushButton_2.clicked.connect(self.getPickedAns)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        
        questionText = self.userObject.question
        temp = questionText.split(" ")
        mid = int(len(temp) / 3) 
        line1 = " ".join(temp[ 0:mid ])
        line2 = " ".join(temp[ mid:(2*mid) ])
        line3 = " ".join(temp[ 2*mid:len(temp) ])
        
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">"+line1+"</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">"+line2+"</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">"+line3+"</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">"+self.userObject.deckName+"</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">♦</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "END GAME"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PICK YOUR ANSWER :</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0c0383;\">♦</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0c0383;\">♦</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0c0383;\">♦</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0c0383;\">♦</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0c0383;\">♦</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0c0383;\">♦</span></p></body></html>"))




#class User(object):
#    userName = ""
#    server = False
#    gameCode = ""
#    deckName = ""
#    questionNo = 0
#    question = ""
#
#userObject = User()
#userObject.deckName = "deckname"
#userObject.question = "what is your naem"
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Dialog = QtWidgets.QDialog()
#    ui = Ui_Dialog5()
#    ui.setupUi(Dialog, userObject)
#    Dialog.show()
#    sys.exit(app.exec_())

