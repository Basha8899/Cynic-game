    # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled7.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog7(object):
    def checkCode(self):
        import pymongo as pm
        client = pm.MongoClient('localhost', 27017)
        db = client['psych']
        hostCode = db['hostCodes']
        x = self.plainTextEdit.toPlainText()
        
        output = str(hostCode.find_one({'code':x}))
        if( output == 'None' ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('WRONG CODE')
            error_dialog.exec_()                        
        else:
            output = hostCode.find_one({'code':x})
#            #serverIp = output['ip']
            self.userObject.gameCode = x
            self.userObject.deckName = output['deckName']
            self.userObject.server = False
#            upDatePlayer = db[self.userObject.gameCode]
#            import socket
#            self.userObject.ipAddress =  socket.gethostname()
#            
#            upDatePlayer.insert({'ip':self.userObject.ipAddress, 'playerName':self.userObject.userName,'points':0,'aswer':"null"})
#            
            
    def setupUi(self, Dialog, userObject):
        self.userObject = userObject
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 534)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 0, 281, 81))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 601, 111))
        self.graphicsView.setStyleSheet("background-color: rgb(0, 57, 173);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 141, 91))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 120, 591, 141))
        self.label_3.setObjectName("label_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 110, 601, 431))
        self.graphicsView_2.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 470, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(450, 480, 55, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(120, 480, 55, 31))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 290, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(4, 4, 4);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.graphicsView_2.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.plainTextEdit.raise_()
        self.pushButton.clicked.connect(self.checkCode)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">JOIN A GAME</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; color:#f5f5f5;\">♣</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">AWKWARDLY STARE AT THE LEADER UNTIL</span></p><p align=\"center\"><span style=\" font-size:16pt;\">THEY TELL YOU THE SECRET CODE.</span></p><p align=\"center\"><span style=\" font-size:16pt;\">THEN ENTER IT HERE:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "SUBMIT"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#f8f8f8;\">◘</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#f8f8f8;\">◘</span></p></body></html>"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Dialog = QtWidgets.QDialog()
#    ui = Ui_Dialog7()
#    ui.setupUi(Dialog)
#    Dialog.show()
#    sys.exit(app.exec_())

