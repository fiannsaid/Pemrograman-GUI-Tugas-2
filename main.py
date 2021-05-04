# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Data):
        Data.setObjectName("Data")
        Data.resize(607, 597)
        self.label = QtWidgets.QLabel(Data)
        self.label.setGeometry(QtCore.QRect(230, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        #Data Mahasiswa
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Data)
        self.label_2.setGeometry(QtCore.QRect(60, 410, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        #NIM
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Data)
        self.lineEdit.setGeometry(QtCore.QRect(130, 410, 401, 20))
        self.lineEdit.setObjectName("lineEdit")

        #Nama
        self.lineEdit_2 = QtWidgets.QLineEdit(Data)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 440, 401, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Data)
        self.label_3.setGeometry(QtCore.QRect(60, 440, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        #Jurusan
        self.lineEdit_3 = QtWidgets.QLineEdit(Data)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 470, 401, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Data)
        self.label_4.setGeometry(QtCore.QRect(60, 470, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        #No.Telp
        self.lineEdit_4 = QtWidgets.QLineEdit(Data)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 500, 401, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Data)
        self.label_5.setGeometry(QtCore.QRect(60, 500, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        #Button TAMBAH
        self.pushButton = QtWidgets.QPushButton(Data)
        self.pushButton.setGeometry(QtCore.QRect(210, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #Button EDIT
        self.pushButton_2 = QtWidgets.QPushButton(Data)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        #Button CLEAR
        self.pushButton_3 = QtWidgets.QPushButton(Data)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        #Button HAPUS
        self.pushButton_4 = QtWidgets.QPushButton(Data)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        #Hasil
        self.listWidget = QtWidgets.QListWidget(Data)
        self.listWidget.setGeometry(QtCore.QRect(60, 80, 471, 311))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Data)
        QtCore.QMetaObject.connectSlotsByName(Data)

    def retranslateUi(self, Data):
        _translate = QtCore.QCoreApplication.translate
        Data.setWindowTitle(_translate("Data", "Form"))
        self.label.setText(_translate("Data", "Data Mahasiswa"))
        self.label_2.setText(_translate("Data", "NIM"))
        self.label_3.setText(_translate("Data", "Nama"))
        self.label_4.setText(_translate("Data", "Jurusan"))
        self.label_5.setText(_translate("Data", "No.Telp"))
        self.pushButton.setText(_translate("Data", "TAMBAH"))
        self.pushButton_2.setText(_translate("Data", "EDIT"))
        self.pushButton_3.setText(_translate("Data", "CLEAR"))
        self.pushButton_4.setText(_translate("Data", "HAPUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

