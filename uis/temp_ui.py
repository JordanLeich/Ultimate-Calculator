from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class TemperatureWindow(QMainWindow):
    def __init__(self, path=""):
        super(TemperatureWindow, self).__init__()

        self.path = f"{path}Ui_Base/temp.ui"
        loadUi(self.path, self)

        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = TemperatureWindow()
    window.show()
    sys.exit(app.exec_())
