import sys
import pymongo as pm

from PyQt5 import QtWidgets
from unti1 import Ui_Dialog 
from unti2 import Ui_Dialog2
from unti3 import Ui_Dialog3
from unti4 import Ui_Dialog4
from unti5 import Ui_Dialog5
from unti6 import Ui_Dialog6
from unti7 import Ui_Dialog7
class User(object):
    userName = ""
    server = True
    gameCode = ""
    deckName = ""
    questionNo = 0
    question = ""
    ipAddress = ''
    pickedans = ""
userObject = User()

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
app.exec_()


app2 = QtWidgets.QApplication(sys.argv)
Dialog2 = QtWidgets.QDialog()
ui2 = Ui_Dialog2()
ui2.setupUi(Dialog2, userObject)
Dialog2.show()
app2.exec_()

   
if userObject.server == False:
    app7 = QtWidgets.QApplication(sys.argv)
    Dialog7 = QtWidgets.QDialog()
    ui7 = Ui_Dialog7()
    ui7.setupUi(Dialog7, userObject)
    Dialog7.show()
    app7.exec_()

app3 = QtWidgets.QApplication(sys.argv)
Dialog3 = QtWidgets.QDialog()
ui3 = Ui_Dialog3()
ui3.setupUi(Dialog3, userObject)
Dialog3.show()
app3.exec_()

app4 = QtWidgets.QApplication(sys.argv)
Dialog4 = QtWidgets.QDialog()
ui4 = Ui_Dialog4()
ui4.setupUi(Dialog4, userObject)
Dialog4.show()
app4.exec_()

app5 = QtWidgets.QApplication(sys.argv)
Dialog5 = QtWidgets.QDialog()
ui5 = Ui_Dialog5()
ui5.setupUi(Dialog5, userObject)
Dialog5.show()
app5.exec_()

app6 = QtWidgets.QApplication(sys.argv)
Dialog6 = QtWidgets.QDialog()
ui6 = Ui_Dialog6()
ui6.setupUi(Dialog6, userObject)
Dialog6.show()
app6.exec_()

client = pm.MongoClient('localhost', 27017)
db = client['psych']
collection = db[userObject.gameCode]    
collection.drop()

collection = db['hostCodes']
collection.delete_one({'code':userObject.gameCode})

