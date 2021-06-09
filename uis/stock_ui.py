from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class StockWindow(QMainWindow):
    def __init__(self, path=""):
        super(StockWindow, self).__init__()

        self.path = f"{path}Ui_Base/stock.ui"
        loadUi(self.path, self)

        self.go_btn.clicked.connect(self.stock)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = StockWindow()
    window.show()
    sys.exit(app.exec_())
