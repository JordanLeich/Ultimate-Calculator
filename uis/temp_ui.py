from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TempWindow(object):
    def convert(self):
        try:
            degree = float(self.line1.text())
            from_ = self.comboBox1.currentText()
            to = self.comboBox.currentText()
            if from_ == 'Celsius':
                if to == 'Celsius':
                    output = degree
                    self.line2.setText(str(output) + ' Celsius')
                elif to == 'Fahrenheit':
                    output = degree * 1.8 + 32
                    self.line2.setText(str(output) + ' Fahrenheit')
                elif to == 'Kelvin':
                    output = degree + 273.15
                    self.line2.setText(str(output) + ' Kelvin')
            elif from_ == 'Fahrenheit':
                if to == 'Fahrenheit':
                    output = degree
                    self.line2.setText(str(output) + ' Fahrenheit')
                elif to == 'Celsius':
                    output = (degree - 32) * 5/9
                    self.line2.setText(str(output) + ' Celsius')
                elif to == 'Kelvin':
                    output = (degree - 32) * 5 / 9 + 273.15
                    self.line2.setText(str(output) + ' Kelvin')
            elif from_ == 'Kelvin':
                if to == 'Kelvin':
                    output = degree
                    self.line2.setText(str(output) + ' Kelvin')
                elif to == 'Celsius':
                    output = degree - 273.15
                    self.line2.setText(str(output) + ' Celsius')
                elif to == 'Fahrenheit':
                    output = (degree - 273.15) * 1.8 + 32
                    self.line2.setText(str(output) + ' Fahrenheit')
        except:
            self.line2.setText("Try again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(190, 20, 201, 41))
        self.line1.setObjectName("line1")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(190, 90, 201, 31))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(190, 220, 201, 41))
        self.line2.setObjectName("line2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 121, 31))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 150, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.cvt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cvt_btn.setGeometry(QtCore.QRect(50, 320, 161, 51))
        self.cvt_btn.setObjectName("cvt_btn")
        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(270, 320, 161, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Celsius"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Fahrenheit"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "Kelvin"))
        self.label.setText(_translate("MainWindow", "Temperature Degree"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Celsius"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fahrenheit"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Kelvin"))
        self.cvt_btn.setText(_translate("MainWindow", "Convert"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TempWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
