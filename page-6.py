# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled6.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog6(object):
    def setupUi(self, Dialog, userObject):
        self.userObject = userObject
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 813)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 0, 201, 81))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 681, 91))
        self.graphicsView.setStyleSheet("background-color: rgb(0, 51, 153);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 611, 171))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 270, 611, 31))
        self.line.setStyleSheet("color: rgb(0, 52, 156);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 230, 55, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 290, 511, 111))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 670, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(20, 12, 131);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 740, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(5, 13, 170);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 390, 621, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(127, 127, 127);")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(8)
        self.listWidget.setObjectName("listWidget")
        
        #database connection
        import pymongo as pm
        client = pm.MongoClient('localhost', 27017)
        db = client['psych']
        display = db[self.userObject.gameCode]
        entries = []
        for i in display.find():
            entries.append( i['playerName']+" : "+str(i['points']))
        self.listWidget.addItems(entries)
            
        
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 90, 681, 731))
        self.graphicsView_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 370, 621, 41))
        self.line_2.setStyleSheet("color: rgb(0, 52, 156);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(8)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(30, 610, 621, 41))
        self.line_3.setStyleSheet("color: rgb(0, 52, 156);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(8)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(10, 390, 31, 241))
        self.line_4.setStyleSheet("color: rgb(0, 45, 135);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(8)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(640, 390, 31, 241))
        self.line_5.setStyleSheet("color: rgb(0, 45, 135);")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(8)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.graphicsView_2.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.listWidget.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">RESULTS </span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#616161;\">YOU PICKED UP</span></p><p align=\"center\"><span style=\" font-size:22pt; color:#616161;\">"+self.userObject.pickedans+"</span></p><p align=\"center\"><span style=\" font-size:22pt; color:#616161;\">ANSWER</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#002d88;\">♠</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">HOW MANY TIMES WAS EACH </span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">ANSWER PICKED</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "READY"))
        self.pushButton_2.setText(_translate("Dialog", "END GAME"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Dialog = QtWidgets.QDialog()
#    ui = Ui_Dialog6()
#    ui.setupUi(Dialog)
#    Dialog.show()
#    sys.exit(app.exec_())

