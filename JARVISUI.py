# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JARVISUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_JARVIS(object):
    def setupUi(self, JARVIS):
        JARVIS.setObjectName("JARVIS")
        JARVIS.resize(936, 572)
        self.centralwidget = QtWidgets.QWidget(JARVIS)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 591))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("textBrowser{\n"
"    background:transparent;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("212508.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 500, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"   background-color:rgb(74, 171, 255);\n"
"  border-radius:5px;\n"
"}\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 500, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"   background-color:rgb(255, 255, 255);\n"
"  border-radius:5px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 391, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("T8bahf.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 390, 481, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("vr.gif"))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(490, 30, 161, 41))
        self.textBrowser.setStyleSheet("background:transparent;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(670, 30, 161, 41))
        self.textBrowser_2.setStyleSheet("background:transparent;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        JARVIS.setCentralWidget(self.centralwidget)

        self.retranslateUi(JARVIS)
        QtCore.QMetaObject.connectSlotsByName(JARVIS)

    def retranslateUi(self, JARVIS):
        _translate = QtCore.QCoreApplication.translate
        JARVIS.setWindowTitle(_translate("JARVIS", "MainWindow"))
        self.pushButton.setText(_translate("JARVIS", "RUN"))
        self.pushButton_2.setText(_translate("JARVIS", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JARVIS = QtWidgets.QMainWindow()
    ui = Ui_JARVIS()
    ui.setupUi(JARVIS)
    JARVIS.show()
    sys.exit(app.exec_())
