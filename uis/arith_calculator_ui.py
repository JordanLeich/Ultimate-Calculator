from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication


class Arithmetic(QWidget):
    def __init__(self, path=""):
        super(Arithmetic, self).__init__()

        self.path = f"{path}Ui_Base/arith_calculator.ui"
        loadUi(self.path, self)

        self.only_int = QIntValidator()
        self.lineEdit.setValidator(self.only_int)
        self.lineEdit.setReadOnly(True)

        self.add.clicked.connect(self.addition)
        self.subtract.clicked.connect(self.subtraction)
        self.multiply.clicked.connect(self.multiplication)
        self.divide.clicked.connect(self.division)
        self.equal.clicked.connect(self.equals)
        self.clear.clicked.connect(self.lineEdit.clear)
        self.exit.clicked.connect(self.hide)

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

    def power(self):
        self.lineEdit.insert(" ** ")

    def division(self):
        self.lineEdit.insert(" / ")

    def left_bracket(self):
        self.lineEdit.insert("(")

    def right_bracket(self):
        self.lineEdit.insert(")")

    def equals(self):
        calculation = self.lineEdit.text()
        try:
            answer = eval(calculation)
            self.lineEdit.setText(str(answer))
        except SyntaxError:
            print("Error")

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

        elif key == "(":
            self.left_bracket()

        elif key == ")":
            self.right_bracket()

        elif key == "^":
            self.power()

        elif event.key() == 16777219:  # Key Code for Backspace
            if len(self.lineEdit.text()) == 0:
                return

            if self.lineEdit.text()[-1] == " ":  # Backspace two times if last text is blank/space
                self.lineEdit.backspace()

            self.lineEdit.backspace()

        elif event.key() == 16777220:  # Key Code for Enter
            self.equals()


class Test(QWidget):
    def __init__(self):
        super(Test, self).__init__()
        loadUi("arith_calculator.ui", self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Arithmetic()
    win.show()
    sys.exit(app.exec_())
