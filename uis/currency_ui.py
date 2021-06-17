from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from modules.currency_api import get_currency
import os

class CurrencyWindow(QMainWindow):
    def __init__(self, path=""):
        super(CurrencyWindow, self).__init__()

        self.path = f"{path}Ui_Base/currency.ui"
        loadUi(self.path, self)

        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn.clicked.connect(self.hide)

    def convert(self):
        api_key = os.environ.get('API_KEY')
        amount = float(self.lineEdit.text())
        from_ = self.comboBox.currentText()
        to = self.comboBox_2.currentText()
        if from_ == 'American Dollars USD':
            if to == 'American Dollars USD':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("USD_JPY", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("USD_CAD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("USD_MAD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("USD_EUR", api_key))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Japanese YEN':
            if to == 'Japanese YEN':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("JPY_USD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("JPY_CAD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("JPY_MAD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("JPY_EUR", api_key))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Canadian Dollars CAD':
            if to == 'Canadian Dollars CAD':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("CAD_USD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("CAD_JPY", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("CAD_MAD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("CAR_EUR", api_key))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Moroccan MAD':
            if to == 'Moroccan MAD':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("MAD_USD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("MAD_JPY", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("MAD_CAD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Euro':
                output = float(amount * get_currency("MAD_EUR", api_key))
                self.lineEdit_2.setText(str(output))
        elif from_ == 'Euro':
            if to == 'Euro':
                output = amount
                self.lineEdit_2.setText(str(output))
            elif to == 'American Dollars USD':
                output = float(amount * get_currency("EUR_USD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Japanese YEN':
                output = float(amount * get_currency("EUR_JPY", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Canadian Dollars CAD':
                output = float(amount * get_currency("EUR_CAD", api_key))
                self.lineEdit_2.setText(str(output))
            elif to == 'Moroccan MAD':
                output = float(amount * get_currency("EUR_MAD", api_key))
                self.lineEdit_2.setText(str(output))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CurrencyWindow()
    window.show()
    sys.exit(app.exec_())
