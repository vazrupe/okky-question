from util import get_nums


class Stock:
    def __init__(self):
        self.stock = 0
        self.margin = 0

    def buy(self, price):
        self.stock += 1
        self.margin -= price

    def sell(self, price, num_stock=None):
        if num_stock is None:
            num_stock = self.stock
        self.stock -= num_stock
        self.margin += price * num_stock


def get_best_margin(forecasted_stocks):
    stocks = forecasted_stocks
    st = Stock()

    days = len(stocks)
    last_day = days - 1

    sell_timing, sell_price = get_sell_timing_price(stocks)
    for day in range(days):
        this_price = stocks[day]
        is_last_day = day == (days - 1)
        if is_last_day:
            st.sell(this_price)
            break
        
        do_sell = day == sell_timing
        do_buy = day < sell_timing and this_price < sell_price
        if do_sell:
            st.sell(this_price)
            (sell_timing, 
            sell_price) = get_sell_timing_price(stocks, sell_timing)
        elif do_buy:
            st.buy(this_price)
    return st.margin


def get_sell_timing_price(stocks, last_timing=-1):
    timing = stocks[last_timing+1:].index(max(stocks[last_timing+1:]))
    timing += last_timing + 1
    price = stocks[timing]

    return timing, price


if __name__ == '__main__':
    t = int(input())

    t_stocks = []
    for _ in range(t):
        n = int(input())

        t_stocks.append([price for price in get_nums(n)])

    for margin in map(get_best_margin, t_stocks):
        print(margin)
