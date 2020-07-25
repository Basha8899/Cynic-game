# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(717, 647)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 580, 311, 51))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 10, 381, 101))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-10, 0, 801, 651))
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setStyleSheet("border-image : url(cynic.png)1 0 0 0 stretch stretch;")
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 130, 371, 41))
        self.label_2.setObjectName("label_2")
        
        self.graphicsView.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Let's Play"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">***LAUNCHING GAME***</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:48pt; color:#000000;\">CYNIC!</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">OUTFOX YOUR FRIENDS</span></p><p><span style=\" font-size:14pt; color:#ffffff;\"><br/></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

