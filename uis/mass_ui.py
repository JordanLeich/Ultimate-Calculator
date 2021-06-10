from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class MassWindow(QMainWindow):
    def __init__(self, path=""):
        super(MassWindow, self).__init__()

        self.path = f"{path}Ui_Base/mass.ui"
        loadUi(self.path, self)

        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MassWindow()
    window.show()
    sys.exit(app.exec_())
