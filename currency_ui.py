from PyQt5 import QtCore, QtGui, QtWidgets
from currency_api import get_currency


class Ui_CurrencyWindow(object):
    def convert(self):
        amount = float(self.lineEdit.text())
        from_ = self.comboBox.currentText()
        to = self.comboBox_2.currentText()
        if from_ == 'American Dollars USD':
            if to == 'American Dollars USD':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("USD_JPY"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("USD_CAD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("USD_MAD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("USD_EUR"))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Japanese YEN':
            if to == 'Japanese YEN':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("JPY_USD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("JPY_CAD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("JPY_MAD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("JPY_EUR"))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Canadian Dollars CAD':
            if to == 'Canadian Dollars CAD':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("CAD_USD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("CAD_JPY"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("CAD_MAD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("CAR_EUR"))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Moroccan MAD':
            if to == 'Moroccan MAD':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("MAD_USD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("MAD_JPY"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("MAD_CAD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("MAD_EUR"))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Euro':
            if to == 'Euro':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("EUR_USD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("EUR_JPY"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("EUR_CAD"))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("EUR_MAD"))
                self.lineEdit_2.setText(str(output))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 241, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 131, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 90, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 131, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 150, 241, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 131, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 220, 241, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 220, 131, 31))
        self.label_4.setObjectName("label_4")
        self.cvt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cvt_btn.setGeometry(QtCore.QRect(110, 312, 151, 51))
        self.cvt_btn.setObjectName("cvt_btn")
        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(350, 310, 151, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Currency Converter"))
        self.label.setText(_translate("MainWindow", "Amount of Money"))
        self.comboBox.setItemText(0, _translate(
            "MainWindow", "American Dollars USD"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Japanese YEN"))
        self.comboBox.setItemText(2, _translate(
            "MainWindow", "Canadian Dollars CAD"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Euro"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Moroccan MAD"))
        self.label_2.setText(_translate("MainWindow", "Convert From"))
        self.comboBox_2.setItemText(0, _translate(
            "MainWindow", "American Dollars USD"))
        self.comboBox_2.setItemText(
            1, _translate("MainWindow", "Japanese YEN"))
        self.comboBox_2.setItemText(2, _translate(
            "MainWindow", "Canadian Dollars CAD"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Euro"))
        self.comboBox_2.setItemText(
            4, _translate("MainWindow", "Moroccan MAD"))
        self.label_3.setText(_translate("MainWindow", "Convert To"))
        self.label_4.setText(_translate("MainWindow", "Output"))
        self.cvt_btn.setText(_translate("MainWindow", "Convert"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CurrencyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
