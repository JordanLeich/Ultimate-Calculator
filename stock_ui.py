
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StockWindow(object):
    def stock(self):
        user_shares = float(self.lineEdit.text())
        user_purchase_price = float(self.lineEdit_2.text())
        user_sell_price = float(self.lineEdit_3.text())

        try:
            user_buy_commission = float(self.lineEdit_4.text())
            user_sell_commission = float(self.lineEdit_5.text())
            user_gain_loss = ((user_sell_price * user_shares) - user_sell_commission) - (
                (user_purchase_price * user_shares) + user_buy_commission)
            self.lineEdit_6.setText(str(user_gain_loss)+' Dollars')
        except:
            user_gain_loss = (user_sell_price * user_shares) - (
                (user_purchase_price * user_shares))
            self.lineEdit_6.setText(str(user_gain_loss)+' Dollars')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 19, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 70, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 130, 241, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 180, 241, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 230, 241, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 290, 241, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_btn.setGeometry(QtCore.QRect(110, 360, 121, 51))
        self.go_btn.setObjectName("go_btn")
        self.go_btn.clicked.connect(self.stock)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(360, 360, 121, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 121, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 121, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 121, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 121, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 220, 121, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 280, 121, 41))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Shares"))
        self.go_btn.setText(_translate("MainWindow", "Go"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Number of Shares"))
        self.label_2.setText(_translate("MainWindow", "Purchase Price"))
        self.label_3.setText(_translate("MainWindow", "Sell Price"))
        self.label_4.setText(_translate("MainWindow", "Buy Commission"))
        self.label_5.setText(_translate("MainWindow", "Sell Commission"))
        self.label_6.setText(_translate("MainWindow", "Profit Gain/Loss"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QDialog(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_StockWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
