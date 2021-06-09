from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class VolumeWindow(QMainWindow):
    def __init__(self):
        super(VolumeWindow, self).__init__()
        loadUi("uis/Ui_Base/volume.ui", self)

        self.exit_btn.clicked.connect(self.hide)
        self.cvt_btn.clicked.connect(self.convert)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = VolumeWindow()
    window.show()
    sys.exit(app.exec_())
