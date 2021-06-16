from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from modules.currency_api import get_currency


class CurrencyWindow(QMainWindow):
    def __init__(self, path=""):
        super(CurrencyWindow, self).__init__()

        self.path = f"{path}Ui_Base/currency.ui"
        loadUi(self.path, self)

        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CurrencyWindow()
    window.show()
    sys.exit(app.exec_())
