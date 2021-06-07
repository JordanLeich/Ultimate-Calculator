
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LengthWindow(object):
    def convert(self):
        try:
            length = float(self.line1.text())
            from_ = self.comboBox1.currentText()
            to = self.comboBox2.currentText()
            if from_ == 'Feet':
                if to == 'Feet':
                    output = length
                    self.line2.setText(str(output))
                elif to == 'Inch':
                    output = length * 12
                    self.line2.setText(str(output))
                elif to == 'Yard':
                    output = length / 3
                    self.line2.setText(str(output))
                elif to == 'Mile':
                    output = length / 5280
                    self.line2.setText(str(output))
            if from_ == 'Inch':
                if to == 'Inch':
                    output = length
                    self.line2.setText(str(output))
                elif to == 'Feet':
                    output = length / 12
                    self.line2.setText(str(output))
                elif to == 'Yard':
                    output = length / 36
                    self.line2.setText(str(output))
                elif to == 'Mile':
                    output = length / 63360
                    self.line2.setText(str(output))
            if from_ == 'Yard':
                if to == 'Yard':
                    output = length
                    self.line2.setText(str(output))
                elif to == 'Feet':
                    output = length * 3
                    self.line2.setText(str(output))
                elif to == 'Inch':
                    output = length * 36
                    self.line2.setText(str(output))
                elif to == 'Mile':
                    output = length / 1760
                    self.line2.setText(str(output))
            if from_ == 'Mile':
                if to == 'Mile':
                    output = length
                    self.line2.setText(str(output))
                elif to == 'Feet':
                    output = length * 5280
                    self.line2.setText(str(output))
                elif to == 'Inch':
                    output = length * 63360
                    self.line2.setText(str(output))
                elif to == 'Yard':
                    output = length * 1760
                    self.line2.setText(str(output))
        except:
            self.line2.setText("Try Again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 210, 121, 31))
        self.label_4.setObjectName("label_4")
        self.cvt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cvt_btn.setGeometry(QtCore.QRect(60, 320, 161, 51))
        self.cvt_btn.setObjectName("cvt_btn")
        self.cvt_btn.clicked.connect(self.convert)
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(200, 10, 201, 41))
        self.line1.setObjectName("line1")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(280, 320, 161, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 121, 31))
        self.label_2.setObjectName("label_2")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(200, 210, 201, 41))
        self.line2.setObjectName("line2")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(200, 80, 201, 31))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 121, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(200, 140, 201, 31))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Length Converter"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.cvt_btn.setText(_translate("MainWindow", "Convert"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Feet"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Inch"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "Yard"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "Mile"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Feet"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Inch"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "Yard"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "Mile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LengthWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
