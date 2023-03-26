# import modules
from binance.client import Client
import pandas as pd

# input api and api secret key from binance
api_key = ""
api_secret_key = ""
# defines user as client, takes in api_key, api_secret_key, testnet
client = Client(api_key, api_secret_key, tld="com", testnet=True)

# defines class as BOT
class BOT:
    # defines parameters of class
    def __init__(self, symbol, volume, num_safe_orders, ratio, take_profit):
        self.symbol = symbol
        self.volume = volume
        self.num_safe_orders = num_safe_orders
        self.ratio = ratio
        self.take_profit = take_profit

    # function for getting balance of user
    def get_bal(self):
        x = client.get_account()
        df = pd.Dataframe(x['balances'])

    # function for getting current price
    def get_actual_value(self, symbol):
        price = client.get_symbol_ticker(symbol=symbol)
        return price["price"]

    # function for placing order
    def market_order(self,symbol, volume, direction):
        if direction == "buy":
            order = client.create_order(
                symbol=symbol,
                side=Client.SIDE_BUY,
                type=Client.ORDER_TYPE_MARKET,
                quantity=volume
            )
            return order['fills']

        if direction == "sell":
            order = client.create_order(
                symbol=symbol,
                side=Client.SIDE_SELL,
                type=Client.ORDER_TYPE_MARKET,
                quantity=volume
            )
            print(order['fills'])

    # function for calculating difference from initial price bought
    def cal_dev_from_initial_price(self, symbol, df):
        curr_price = float(self.get_actual_value(symbol))
        init_price = float(df.price[0])
        pct_change = ((curr_price - init_price) / init_price) * 100
        return pct_change

    # function for calculating profit
    def cal_pct_profit(self, symbol, df):
        total_profit = 0
        total_value_of_coins = 0
        current_price = float(self.get_actual_value(symbol))

        # iterates over values in dataframe
        for index in df.index:
            initial_value = float(df.loc[index, "price"] * float(df.loc[index, "qty"]))
            current_value = current_price * float(df.loc[index, "qty"])
            profit = current_value - initial_value
            total_profit += profit
            total_value_of_coins += initial_value
        return (total_profit / total_value_of_coins) * 100

    # function for selling all assets
    def sell_all(self, symbol, df):
        volume = float(df["qty"].sum())
        self.market_order(symbol, volume, "sell")

    # function for continuous running of bot
    def run(self):
        while True:
            df1 = pd.DataFrame(columns=['price', 'qty'])
            df2 = pd.DataFrame(columns=['price', 'qty'])
            x = self.market_order(self, symbol, volume, "buy")
            df2.loc[0, 'price'] = float(x[0]['price'])
            df2.loc[0, 'quantity'] = float(x[0]['qty'])
            df1 = pd.concat([df1, df2], ignore_index=True)

            curr_no_of_safety_orders = 0
            multiplied_volume = self.volume * 2
            deviation = -1
            next_price_level = -1

            while True:
                dev = self.cal_dev_from_initial_price(symbol, df1)
                print(f"Deviation : {dev}")
                if dev <= next_price_level * self.ratio:
                    if curr_no_of_safety_orders < self.num_safe_orders:
                        try:
                            x = self.market_order(self, symbol, volume, "buy")
                            df2.loc[0, 'price'] = float(x[0]['price'])
                            df2.loc[0, 'quantity'] = float(x[0]['qty'])
                            df1 = pd.concat([df1, df2], ignore_index=True)
                        except:
                            pass

                        multiplied_volume *= 2
                        deviation *= 2
                        next_price_level += deviation
                        curr_no_of_safety_orders += 1
                pct_profit = self.cal_pct_profit(self, symbol, df1)
                print(f"pct_profit : {pct_profit}")
                print(df1)
                if pct_profit >= self.take_profit:
                    self.sell_all(symbol, df1)
                    break