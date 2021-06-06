
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VolumeWindow(object):
    def convert(self):
        try:
            volume = float(self.line1.text())
            from_ = self.comboBox1.currentText()
            to = self.comboBox2.currentText()
            if from_ == 'Gallons':
                if to == 'Gallons':
                    output = volume
                    self.line2.setText(str(output))
                elif to == 'Quarts':
                    output = volume * 4
                    self.line2.setText(str(output))
                elif to == 'Pints':
                    output = volume * 8
                    self.line2.setText(str(output))
                elif to == 'Ounces':
                    output = volume * 128
                    self.line2.setText(str(output))
            if from_ == 'Quarts':
                if to == 'Quarts':
                    output = volume
                    self.line2.setText(str(output))
                elif to == 'Gallons':
                    output = volume / 4
                    self.line2.setText(str(output))
                elif to == 'Pints':
                    output = volume * 2
                    self.line2.setText(str(output))
                elif to == 'Ounces':
                    output = volume * 32
                    self.line2.setText(str(output))
            if from_ == 'Pints':
                if to == 'Pints':
                    output = volume
                    self.line2.setText(str(output))
                elif to == 'Gallons':
                    output = volume / 8
                    self.line2.setText(str(output))
                elif to == 'Quarts':
                    output = volume / 2
                    self.line2.setText(str(output))
                elif to == 'Ounces':
                    output = volume * 16
                    self.line2.setText(str(output))
            if from_ == 'Ounces':
                if to == 'Ounces':
                    output = volume
                    self.line2.setText(str(output))
                elif to == 'Gallons':
                    output = volume / 128
                    self.line2.setText(str(output))
                elif to == 'Quarts':
                    output = volume / 32
                    self.line2.setText(str(output))
                elif to == 'Pints':
                    output = volume / 16
                    self.line2.setText(str(output))
        except:
            self.line2.setText("Try Again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 230, 121, 31))
        self.label_4.setObjectName("label_4")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(200, 230, 201, 41))
        self.line2.setObjectName("line2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 121, 31))
        self.label.setObjectName("label")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(280, 340, 161, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(200, 30, 201, 41))
        self.line1.setObjectName("line1")
        self.cvt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cvt_btn.setGeometry(QtCore.QRect(60, 340, 161, 51))
        self.cvt_btn.setObjectName("cvt_btn")
        self.cvt_btn.clicked.connect(self.convert)
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(200, 100, 201, 31))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 121, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(200, 160, 201, 31))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Volume Converter"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label.setText(_translate("MainWindow", "Volume"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.cvt_btn.setText(_translate("MainWindow", "Convert"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Gallons"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Quarts"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "Pints"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "Ounces"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Gallons"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Quarts"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "Pints"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "Ounces"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QDialog(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_VolumeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
