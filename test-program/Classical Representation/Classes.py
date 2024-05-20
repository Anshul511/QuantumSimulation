import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np
import random as rd
import time 

class MonteCarloStock:
    """Lets try to implement Monte Carlo, Price today = Price Yesterday * e^r. r stands for some random stuff"""

    def __init__(self,name):

        self.name = name
        self.curr_price = 0 #this starts at zero, but when a data set is provided it shall change. 
        self.yest_price = 0 #intially starts at zero, might be irrelevant we shall see.
        self.days = 0 #intially zero as well
        self.close_prices = [] #add yesterday_price to all of this
        
        

    """This is the main thing. It should be a way of changing curr_price according to the formula above. UPDATE: This kinda acts as a main 
       and brings all of the helper method stuff together to update curr_price"""

    def update_stock(self,days: int): #generates a simulation after a specific amount of days
        self.days += days # seems like a good thing todo
        trials = 10000
        volatility = np.sqrt(self.get_var()) * norm.ppf(np.random.rand(days, trials))
        drift = self.get_avg() - (0.5 * self.get_var())
        r = volatility + drift
        daily_returns = np.exp(r)
        #NOT DONE

        
        
        

    """Not That Important Just Looks Pretty :)"""
    def generate_stock_chart(self): 
        

        plt.title(f'{self.name}') #names the window correctly
        plt.plot(self.close_prices) 
        plt.ylabel(f"{self.name}'s stock value in USD")
        plt.xlabel("Days")
        plt.show()
        plt.close()
        
    
    def build_total_list(self, list_of_closing_prices: list): #Anshuls Function, it creates the list of past values, made to only be run once
        for val in list_of_closing_prices:
            self.close_prices.append(val)
            self.days += 1
            self.curr_price = self.close_prices[-1]
            self.yest_price = self.close_prices[len(self.close_prices) - 2] # second last one

    def get_avg(self): #Also anshuls function, I think it might be a mistake to put it in here but ill ask mad later.
        """This function returns the average of the data"""

        result = sum(self.close_prices[0:])  / self.days
        return result
    
    def get_var(self):
        """This function returns the variance of the data"""
        summation = 0
        for i in range(len(self.close_prices)):
            summation += (self.close_prices[i] - self.get_avg()) ** 2
        
        result = summation / (len(self.close_prices) - 1)
        return result
    
    
        
        
        
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


"""I think the goal is to achieve Quantum Annealing with these bots, Firstly lets work on making a simulation"""
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
    sma = simple_moving_avg(15, stock) #stands for simple_moving average..
    money_spent = 0
    if sma >= stock.close_prices[-1]:
        money_spent -= 50
    else:
        money_spent += stock.close_prices[-1] * 0.5
    return money_spent
"""Lets work on this later for now lets implement new Stock class"""
def fancy_strategy(stock: Stock) -> float:
    return 0 


if __name__ == "__main__":

    data = pd.read_csv("apple_historical_data.csv")
    close_val = data['Close/Last'].tolist()
    close_val = [price.replace('$', '') for price in close_val]
    close_val = [float(price) for price in close_val]


    
    apple_stock = MonteCarloStock("Apple stock")
    apple_stock.build_total_list(close_val)
    print(f'This is the current value of Apple Stock: {apple_stock.curr_price}')
    apple_stock.generate_stock_chart()
    for i in range(10):
        val_list = [x for x in range(100,200)]
        close_val.append(rd.choice(val_list))

    apple_stock.build_total_list(close_val)
    apple_stock.generate_stock_chart()
    
    

    
