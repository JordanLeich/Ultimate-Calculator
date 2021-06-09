from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class LengthWindow(QMainWindow):
    def __init__(self):
        super(LengthWindow, self).__init__()
        loadUi("uis/Ui_Base/length.ui", self)

        self.cvt_btn.clicked.connect(self.convert)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LengthWindow()
    window.show()
    sys.exit(app.exec_())
