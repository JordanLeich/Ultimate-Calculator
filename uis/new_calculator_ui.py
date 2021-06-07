from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication
from calculators.new_calculator import calculator
from PyQt5.Qt import QIntValidator


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("new_calculator.ui", self)
        self.only_int = QIntValidator()
        self.lineEdit.setValidator(self.only_int)
        self.lineEdit.setReadOnly(True)
        self.add.clicked.connect(self.addition)
        self.subtract.clicked.connect(self.subtraction)
        self.multiply.clicked.connect(self.multiplication)
        self.divide.clicked.connect(self.division)
        self.equal.clicked.connect(self.equals)
        self.clear.clicked.connect(lambda: self.lineEdit.clear())
        self.exit.clicked.connect(lambda: self.hide())

        self.point.clicked.connect(lambda: self.lineEdit.insert("."))
        self.zero.clicked.connect(lambda: self.lineEdit.insert("0"))
        self.one.clicked.connect(lambda: self.lineEdit.insert("1"))
        self.two.clicked.connect(lambda: self.lineEdit.insert("2"))
        self.three.clicked.connect(lambda: self.lineEdit.insert("3"))
        self.four.clicked.connect(lambda: self.lineEdit.insert("4"))
        self.five.clicked.connect(lambda: self.lineEdit.insert("5"))
        self.six.clicked.connect(lambda: self.lineEdit.insert("6"))
        self.seven.clicked.connect(lambda: self.lineEdit.insert("7"))
        self.eight.clicked.connect(lambda: self.lineEdit.insert("8"))
        self.nine.clicked.connect(lambda: self.lineEdit.insert("9"))

    def addition(self):
        self.lineEdit.insert(" + ")

    def subtraction(self):
        self.lineEdit.insert(" - ")

    def multiplication(self):
        self.lineEdit.insert(" * ")

    def division(self):
        self.lineEdit.insert(" / ")

    def equals(self):
        curr_text = self.lineEdit.text().split(" ")
        for ind, text in enumerate(curr_text):
            if text == "":
                curr_text.pop(ind)
        curr_text.append("=")
        calculated = str(calculator(curr_text))
        self.lineEdit.setText(calculated)

    def keyPressEvent(self, event):
        key = event.text()
        if key in [str(i) for i in range(10)]:
            self.lineEdit.insert(key)
        elif key == "+":
            self.addition()
        elif key == "-":
            self.subtraction()
        elif key in ["*", "x"]:
            self.multiplication()
        elif key == "/":
            self.division()
        elif key == "=":
            self.equals()
        elif key == ".":
            self.lineEdit.insert(".")
        elif event.key() == 16777219:
            if self.lineEdit.text()[-1] == " ":
                self.lineEdit.backspace()
            self.lineEdit.backspace()
        elif event.key() == 16777220:
            self.equals()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
