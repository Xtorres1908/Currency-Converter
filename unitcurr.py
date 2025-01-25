
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:#171d1c;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.froml = QtWidgets.QComboBox(self.centralwidget)
        self.froml.setGeometry(QtCore.QRect(100, 280, 121, 41))
        self.froml.setStyleSheet("font: 57 18pt \"LEMON MILK Medium\";\n"
"border:2px solid orange;\n"
"background-color:white;\n"
"border-radius:7px;")
        self.froml.setObjectName("froml")
        self.froml.addItem("")
        self.froml.addItem("")
        self.froml.addItem("")
        self.froml.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 741, 71))
        self.label.setStyleSheet("background-color:white;\n"
"font: 75 italic 24pt \"LEMON MILK Bold\";\n"
"border:2px solid orange;\n"
"border-radius:20px;")
        self.label.setObjectName("label")
        self.tol = QtWidgets.QComboBox(self.centralwidget)
        self.tol.setGeometry(QtCore.QRect(560, 270, 121, 41))
        self.tol.setStyleSheet("font: 57 18pt \"LEMON MILK Medium\";\n"
"border:2px solid orange;\n"
"background-color:white;\n"
"border-radius:7px;")
        self.tol.setObjectName("tol")
        self.tol.addItem("")
        self.tol.addItem("")
        self.tol.addItem("")
        self.tol.addItem("")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(350, 140, 421, 51))
        self.input.setStyleSheet("border:3px solid white;\n"
"font: 75 20pt \"UD Digi Kyokasho NP-B\";\n"
"color:white;")
        self.input.setText("")
        self.input.setObjectName("input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 411, 81))
        self.label_2.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 230, 121, 41))
        self.label_3.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 220, 111, 41))
        self.label_4.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 410, 221, 81))
        self.label_5.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 420, 351, 61))
        self.label_6.setStyleSheet("border:3px solid white;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(310, 340, 141, 41))
        self.convert.setStyleSheet("background-color:white;\n"
"font: 75 12pt \"LEMON MILK Bold\";\n"
"border:2px solid orange;\n"
"border-radius:15px;")
        self.convert.setObjectName("convert")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.froml.setItemText(0, _translate("MainWindow", "USD"))
        self.froml.setItemText(1, _translate("MainWindow", "INR"))
        self.froml.setItemText(2, _translate("MainWindow", "EUR"))
        self.froml.setItemText(3, _translate("MainWindow", "JPY"))
        self.label.setText(_translate("MainWindow", "        Currency Converter"))
        self.tol.setItemText(0, _translate("MainWindow", "USD"))
        self.tol.setItemText(1, _translate("MainWindow", "INR"))
        self.tol.setItemText(2, _translate("MainWindow", "EUR"))
        self.tol.setItemText(3, _translate("MainWindow", "JPY"))
        self.label_2.setText(_translate("MainWindow", "Enter amount :"))
        self.label_3.setText(_translate("MainWindow", "From"))
        self.label_4.setText(_translate("MainWindow", "TO"))
        self.label_5.setText(_translate("MainWindow", "result:"))
        self.convert.setText(_translate("MainWindow", "Convert"))
        self.convert.clicked.connect(self.currency)
        
    def currency(self):
        f=-1
        b=self.froml.currentText()
        c=self.tol.currentText()
        am=self.input.text()
        a=int(am)
        if b=="USD" and c=="INR":
                a=a*86
                f=1
        elif b=="USD" and c=="USD":
                a=a
                f=2
        elif b=="USD" and c=="EUR":
                a=a*0.95
                f=3
        elif b=="USD" and c=="JPY":
                a=a*156
                f=4
        elif b=="INR" and c=="USD":
                a=a*0.012
                f=2
        elif b=="INR" and c=="EUR":
                a=a*0.011
                f=3
        elif b=="INR" and c=="INR":
                a=a
                f=1
        elif b=="INR" and c=="JPY":
                a=a*1.81
                f=4
        elif b=="EUR" and c=="USD":
                a=a*1.05
                f=2
        elif b=="EUR" and c=="EUR":
                a=a
                f=3
        elif b=="EUR" and c=="JPY":
                a=a*163
                f=4
        elif b=="EUR" and c=="INR":
                a=a*90.47
                f=1
                
        elif b=="JPY" and c=="USD":
                a=a*0.0064
                f=2
        elif b=="JPY" and c=="EUR":
                a=a*0.0061
                f=3
        elif b=="JPY" and c=="JPY":
                a=a
                f=4
        elif b=="JPY" and c=="INR":
                a=a*0.55
                f=1
        
        con=str(a)
        if f==1:
                self.label_6.setText('₹'+con)
        elif f==2:
                self.label_6.setText('$'+con)
        elif f==3:
                self.label_6.setText('£'+con)
        elif f==4:
                self.label_6.setText('¥'+con)                   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
