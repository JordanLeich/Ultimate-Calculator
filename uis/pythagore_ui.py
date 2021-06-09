from math import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class PythaWindow(QMainWindow):
    def __init__(self):
        super(PythaWindow, self).__init__()
        loadUi("uis/Ui_Base/pythagore.ui", self)

        self.go_btn.clicked.connect(self.pytha)
        self.exit_btn.clicked.connect(self.hide)

    def pytha(self):
        try:
            side = self.comboBox.currentText()
            if side == "A":
                b = int(self.line_2.text())
                c = int(self.line_3.text())
                a = sqrt(c*c-b*b)
                self.line_1.setText(str(a))
            elif side == "B":
                a = int(self.line_1.text())
                c = int(self.line_3.text())
                b = sqrt(c*c-a*a)
                self.line_2.setText(str(b))
            elif side == "C":
                a = int(self.line_1.text())
                b = int(self.line_2.text())
                c = sqrt(a*a+b*b)
                self.line_3.setText(str(c))
        except:
            self.line_1.setText("Try Again ...!")
            self.line_2.setText("Try Again ...!")
            self.line_3.setText("Try Again ...!")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PythaWindow()
    window.show()
    sys.exit(app.exec_())
