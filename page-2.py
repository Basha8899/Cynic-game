# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    
    def putClientInformation(self):
        if( len(self.lineEdit.text()) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR NAME EMPTY')
            error_dialog.exec_()                        
        else:
            self.userObject.userName = self.lineEdit.text()
            self.userObject.server = False
        
    def putServerInformation1(self):
        if( len(self.lineEdit.text()) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR NAME EMPTY')
            error_dialog.exec_()                        
        else:
            self.userObject.userName = self.lineEdit.text()
            self.userObject.deckName = "MOVIE BLUFF!"
            self.userObject.server = True
    def putServerInformation2(self):
        if( len(self.lineEdit.text()) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR NAME EMPTY')
            error_dialog.exec_()                        
        else:
            self.userObject.userName = self.lineEdit.text()
            self.userObject.deckName = "WORD UP"
            self.userObject.server = True
    def putServerInformation3(self):
        if( len(self.lineEdit.text()) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR NAME EMPTY')
            error_dialog.exec_()                        
        else:
            self.userObject.userName = self.lineEdit.text()
            self.userObject.deckName = "IS THAT A FACT?"
            self.userObject.server = True
    def putServerInformation4(self):
        if( len(self.lineEdit.text()) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR NAME EMPTY')
            error_dialog.exec_()                        
        else:
            self.userObject.userName = self.lineEdit.text()
            self.userObject.deckName = "AND THE TRUTH \nCOMES OUT"
            self.userObject.server = True
    def putServerInformation5(self):
        if( len(self.lineEdit.text()) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR NAME EMPTY')
            error_dialog.exec_()                        
        else:
            self.userObject.userName = self.lineEdit.text()
            self.userObject.deckName = "SAY MY NAME"
            self.userObject.server = True
    def putServerInformation6(self):
        if( len(self.lineEdit.text()) == 0  ):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('YOUR NAME EMPTY')
            error_dialog.exec_()                        
        else:
            self.userObject.userName = self.lineEdit.text()
            self.userObject.deckName = "WORD UP !\nSWITCHEROO"
            self.userObject.server = True
        
    def setupUi(self, Dialog, userObject):
        self.userObject = userObject
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 676)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 50, 381, 101))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 140, 371, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 21, 211, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 741, 192))
        self.graphicsView.setStyleSheet("background-color: rgb(0, 0, 103);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 270, 331, 81))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 210, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 380, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 29, 110, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 490, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(15, 150, 100, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 600, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(218, 139, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 370, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(155, 149, 149, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 600, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 153, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(310, 470, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(190, 78, 78, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_8.setObjectName("pushButton_8")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 190, 621, 491))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 240, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(520, 240, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(520, 210, 61, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(70, 210, 61, 20))
        self.label_8.setObjectName("label_8")
        self.graphicsView_2.raise_()
        self.pushButton.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
#        self.pushButton.clicked.connect(self.check("asdasd"))
        ##
        self.pushButton.clicked.connect(self.putClientInformation)
        
        
        self.pushButton_3.clicked.connect(self.putServerInformation1)
        
        self.pushButton_4.clicked.connect(self.putServerInformation2)
        
        self.pushButton_5.clicked.connect(self.putServerInformation3)
        
        self.pushButton_6.clicked.connect(self.putServerInformation4)
        
        self.pushButton_7.clicked.connect(self.putServerInformation5)
        
        self.pushButton_8.clicked.connect(self.putServerInformation6)

        ##
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">NAME</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">PSYCH!</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">OUTWIT YOUR FRIENDS</span></p><p><span style=\" font-size:14pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">NAME</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">OR IF YOU\'RE THE GAME <br/>LEADER, </span><span style=\" font-size:11pt; font-weight:600;\">START</span><span style=\" font-size:11pt;\"> A GAME FROM<br/>THE DECKS </span><span style=\" font-size:11pt; font-weight:600;\">BELOW.</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>JOIN A GAME</p><p><br/></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p>JOIN A GAME</p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "JOIN A GAME"))
        self.pushButton_3.setText(_translate("Dialog", "MOVIE BLUFF!"))
        self.pushButton_4.setText(_translate("Dialog", "WORD UP"))
        self.pushButton_5.setText(_translate("Dialog", "IS THAT A FACT?"))
        self.pushButton_6.setText(_translate("Dialog", "AND THE TRUTH \n"
"COMES OUT"))
        self.pushButton_7.setText(_translate("Dialog", "SAY MY NAME"))
        self.pushButton_8.setText(_translate("Dialog", "WORD UP !\n"
"SWITCHEROO"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">♣</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">♣</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">♣</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">♣</span></p></body></html>"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Dialog = QtWidgets.QDialog()
#    ui = Ui_Dialog()
#    ui.setupUi(Dialog)
#    Dialog.show()
#    sys.exit(app.exec_())

