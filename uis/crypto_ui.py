from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class CryptoWindow(QMainWindow):
    def __init__(self):
        super(CryptoWindow, self).__init__()
        loadUi("uis/Ui_Base/crypto.ui", self)

        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CryptoWindow()
    window.show()
    sys.exit(app.exec_())
