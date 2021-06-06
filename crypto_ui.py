from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CryptoWindow(object):
    def convert(self):
        try:
            amount = float(self.line1.text())
            from_ = self.comboBox1.currentText()
            to = self.comboBox2.currentText()
            if from_ == 'Bitcoin':
                if to == 'Bitcoin':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Ethereum':
                    output = amount * 13.72
                    self.line2.setText(str(output))
                elif to == 'DogeCoin':
                    output = amount * 95317.32
                    self.line2.setText(str(output))
                elif to == 'SHIBA INU':
                    output = amount * 4.03
                    self.line2.setText(str(output) + ' Billion')
            if from_ == 'Ethereum':
                if to == 'Ethereum':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Bitcoin':
                    output = amount * 0.072
                    self.line2.setText(str(output))
                elif to == 'DogeCoin':
                    output = amount * 6686.2
                    self.line2.setText(str(output))
                elif to == 'SHIBA INU':
                    output = amount * 292.12
                    self.line2.setText(str(output) + ' Million')
            if from_ == 'DogeCoin':
                if to == 'DogeCoin':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Bitcoin':
                    output = amount * 0.00001089
                    self.line2.setText(str(output))
                elif to == 'Ethereum':
                    output = amount * 0.000150
                    self.line2.setText(str(output))
                elif to == 'SHIBA INU':
                    output = amount * 43745
                    self.line2.setText(str(output))
            if from_ == 'SHIBA INU':
                if to == 'SHIBA INU':
                    output = amount
                    self.line2.setText(str(output))
                elif to == 'Bitcoin':
                    output = amount * 0.00000001
                    self.line2.setText(str(output))
                elif to == 'Ethereum':
                    output = amount * 0.0000000012
                    self.line2.setText(str(output))
                elif to == 'DogeCoin':
                    output = amount * 0.000023
                    self.line2.setText(str(output))
        except:
            self.line2.setText("Try Again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(190, 90, 201, 31))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 121, 31))
        self.label.setObjectName("label")
        self.cvt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cvt_btn.setGeometry(QtCore.QRect(50, 330, 161, 51))
        self.cvt_btn.setObjectName("cvt_btn")
        self.cvt_btn.clicked.connect(self.convert)
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(190, 20, 201, 41))
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(190, 220, 201, 41))
        self.line2.setObjectName("line2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 121, 31))
        self.label_4.setObjectName("label_4")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(270, 330, 161, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(190, 150, 201, 31))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crypto Converter"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Bitcoin"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Ethereum"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "DogeCoin"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "SHIBA INU"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.label.setText(_translate("MainWindow", "Amount"))
        self.cvt_btn.setText(_translate("MainWindow", "Convert"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Bitcoin"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Ethereum"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "DogeCoin"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "SHIBA INU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QDialog(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CryptoWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
