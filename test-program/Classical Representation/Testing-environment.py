import Classes
import pandas as pd

data = pd.read_csv("apple_historical_data.csv")
close_val = data['Close/Last'].tolist()
close_val = [price.replace('$', '') for price in close_val]
close_val = [float(price) for price in close_val]

aapl = Classes.Stock("apple")
aapl.build_total_list(close_val)
aapl.return_info()
print()

bot1 = Classes.Bot(1000, Classes.simple_strategy, aapl)
bot1.run()
bot1.return_info()
print()


c1 = Classes.Stock("company1")
c1.build_total_list(list(range(50, 100)))
c1.return_info()
print()


bot2 = Classes.Bot(500, Classes.simple_strategy, c1)
bot2.run()
bot2.return_info()


print(Classes.simple_moving_avg(15, c1))