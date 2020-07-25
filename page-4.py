# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog4(object):
    def writeToDataBase(self):
        #write into dataBase
        answer = self.plainTextEdit.toPlainText()
        if( len(answer) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR ANSWER EMPTY')
            error_dialog.exec_()                        
        else:
            import pymongo as pm
            client = pm.MongoClient('localhost', 27017)
            db = client['psych']
            updateAns = db[self.userObject.gameCode]    
            updateAns.update({'playerName':self.userObject.userName},{'$set':{'answer':answer}})
        
    def setupUi(self, Dialog, userObject):
        self.userObject = userObject
        Dialog.setObjectName("Dialog")
        Dialog.resize(809, 738)
        Dialog.setStyleSheet("color: rgb(225, 225, 225);")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 300, 741, 281))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setCursorWidth(5)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 130, 511, 131))
        self.label.setObjectName("label")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 811, 251))
        self.graphicsView_2.setStyleSheet("background-color: rgb(0, 0, 103);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 721, 71))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 80, 811, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 70, 55, 51))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(-10, 300, 91, 291))
        self.line_2.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(740, 300, 91, 281))
        self.line_3.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(10)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(30, 280, 761, 41))
        self.line_4.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(10)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(40, 560, 751, 51))
        self.line_5.setStyleSheet("color: rgb(20, 20, 127);")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(10)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 560, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(225, 225, 225);\n"
"background-color: rgb(0, 0, 104);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 650, 461, 51))
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
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 250, 811, 491))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.plainTextEdit.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.pushButton.clicked.connect(self.writeToDataBase)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        
        #question from data base
        import pymongo as pm
        client = pm.MongoClient('localhost', 27017)
        db = client['psych']
        name = db[self.userObject.gameCode]
        from random import randint
        randNo = randint(0,1)
        temp = name.find().limit(-1).skip(randNo).next()
        tempName = temp['playerName']
        
        tempDeck = (self.userObject.deckName).replace(" ","")
        tempDeck = tempDeck.replace("\n","")
        question = db[tempDeck]
        tempQuestion = question.find().limit(-1).skip(self.userObject.questionNo).next()
        outputQuestion =  tempQuestion['quest']
        questionText = outputQuestion.replace("USER_NAME", tempName)
        temp = questionText.split(" ")
        mid = int(len(temp) / 3) 
        line1 = " ".join(temp[ 0:mid ])
        line2 = " ".join(temp[ mid:(2*mid) ])
        line3 = " ".join(temp[ 2*mid:len(temp) ])
        
        self.userObject.question = questionText
        
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">"+line1+"</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">"+line2+"</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">"+line3+"</span></p><p align=\"center\"><br/></p></body></html>"))
        title = self.userObject.deckName
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">"+title+"</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">♦</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "submit"))
        self.pushButton_2.setText(_translate("Dialog", "END GAME"))


#if __name__ == "__main__":
#    import sys
#    app4 = QtWidgets.QApplication(sys.argv)
#    Dialog4 = QtWidgets.QDialog()
#    ui4 = Ui_Dialog4()
#    ui4.setupUi(Dialog4, userObject)
#    Dialog4.show()
#    app4.exec_()

