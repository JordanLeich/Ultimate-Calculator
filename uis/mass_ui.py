
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MassWindow(object):
    def convert(self):
        try:
            amount = float(self.line1.text())
            from_ = self.comboBox1.currentText()
            to = self.comboBox1_2.currentText()
            if from_ == 'Kilogram':
                if to == 'Kilogram':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Grams':
                    output = amount * 1000
                    self.line2.setText(str(output))
                elif to == 'Pounds':
                    output = amount * 2.205
                    self.line2.setText(str(output))
                elif to == 'Ounces':
                    output = amount * 35.274
                    self.line2.setText(str(output))
            if from_ == 'Grams':
                if to == 'Grams':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Kilogram':
                    output = amount / 1000
                    self.line2.setText(str(output))
                elif to == 'Pounds':
                    output = amount / 454
                    self.line2.setText(str(output))
                elif to == 'Ounces':
                    output = amount / 28.35
                    self.line2.setText(str(output))
            if from_ == 'Pounds':
                if to == 'Pounds':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Kilogram':
                    output = amount / 2.205
                    self.line2.setText(str(output))
                elif to == 'Grams':
                    output = amount * 454
                    self.line2.setText(str(output))
                elif to == 'Ounces':
                    output = amount * 16
                    self.line2.setText(str(output))
            if from_ == 'Ounces':
                if to == 'Ounces':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Kilogram':
                    output = amount / 35.274
                    self.line2.setText(str(output))
                elif to == 'Grams':
                    output = amount * 28.35
                    self.line2.setText(str(output))
                elif to == 'Pounds':
                    output = amount / 16
                    self.line2.setText(str(output))
        except:
            self.line2.setText("Try Again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(200, 10, 201, 41))
        self.line1.setObjectName("line1")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(200, 80, 201, 31))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1_2.setGeometry(QtCore.QRect(200, 140, 201, 31))
        self.comboBox1_2.setObjectName("comboBox1_2")
        self.comboBox1_2.addItem("")
        self.comboBox1_2.addItem("")
        self.comboBox1_2.addItem("")
        self.comboBox1_2.addItem("")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(200, 210, 201, 41))
        self.line2.setObjectName("line2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 210, 121, 31))
        self.label_4.setObjectName("label_4")
        self.cvt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cvt_btn.setGeometry(QtCore.QRect(60, 320, 161, 51))
        self.cvt_btn.setObjectName("cvt_btn")
        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(280, 320, 161, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mass Converter"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Kilogram"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Ounces"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "Pounds"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "Grams"))
        self.comboBox1_2.setItemText(0, _translate("MainWindow", "Kilogram"))
        self.comboBox1_2.setItemText(1, _translate("MainWindow", "Ounces"))
        self.comboBox1_2.setItemText(2, _translate("MainWindow", "Pounds"))
        self.comboBox1_2.setItemText(3, _translate("MainWindow", "Grams"))
        self.label.setText(_translate("MainWindow", "Mass"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.cvt_btn.setText(_translate("MainWindow", "Convert"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QDialog(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MassWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
