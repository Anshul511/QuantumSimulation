class Stock:
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.days = 0
        self.close_prices = []

    def update_stock(self, switch: int, val: float):
        self.days += 1
        if switch == 1:
            self.price += val
            self.close_prices.append(self.price)

        else:
            self.price -= val
            self.close_prices.append(self.price)

    def build_total_list(self, list_of_closing_prices: list):
        for val in list_of_closing_prices:
            self.close_prices.append(val)
            self.days += 1
            self.price = self.close_prices[-1]

    def return_info(self):
        print(self.name + "\n" + "price:" + str(self.price) + "\n" + "days:" + str(self.days))

    def reset(self):
        self.price = 0
        self.days = 0
        self.close_prices = []

def simple_moving_avg(days: int, stock: Stock) -> float:
    return sum(stock.close_prices[days:]) / days

class Bot:
    def __init__(self, buying_power: float, strategy, stock: Stock):
        self.buying_power = buying_power
        self.strategy = strategy
        self.trades = []
        self.stock = stock
        self.profit_or_loss = 0

    def run(self):
        self.buying_power += self.strategy(self.stock)
        self.trades.append(self.strategy(self.stock))

    def return_info(self):
        print("trades:", self.trades)
        print("buying power:", self.buying_power)
        print("stock:", self.stock.name)

def simple_strategy(stock: Stock) -> float:
    sma = simple_moving_avg(15, stock)
    money_spent = 0
    if sma >= stock.close_prices[-1]:
        money_spent -= 50
    else:
        money_spent += stock.close_prices[-1] * 0.5
    return money_spent

