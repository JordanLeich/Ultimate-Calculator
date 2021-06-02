import colors
import restart


def start():
    user_shares = float(input('Number of Shares: '))
    user_purchase_price = float(input('Purchase Price ($): '))
    user_sell_price = float(input('Sell Price ($): '))
    user_buy_commission = float(input('Buy Commission (if none, put 0): '))
    user_sell_commission = float(input('Sell Commission (if none, put 0): '))
    print()
    results(user_shares, user_sell_commission, user_buy_commission, user_sell_price, user_purchase_price)


def results(user_shares, user_sell_commission, user_buy_commission, user_sell_price, user_purchase_price):
    user_gain_loss = ((user_sell_price * user_shares) - user_sell_commission) - (
            (user_purchase_price * user_shares) + user_buy_commission)

    print(colors.green + 'Profit gain/loss:', user_gain_loss, 'Dollars.', colors.reset, '\n')
    restart.restart()
