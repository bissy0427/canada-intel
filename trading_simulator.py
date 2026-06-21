import pandas as pd

class PortfolioSimulator:
    def __init__(self, cash=100000):
        self.cash = cash
        self.positions = {}

    def buy(self, ticker, price, quantity):
        cost = price * quantity

        if cost > self.cash:
            return "Insufficient cash"

        self.cash -= cost
        self.positions[ticker] = self.positions.get(ticker, 0) + quantity

        return f"Bought {quantity} of {ticker}"

    def sell(self, ticker, price, quantity):
        if ticker not in self.positions:
            return "No position"

        self.positions[ticker] -= quantity
        self.cash += price * quantity

        return f"Sold {quantity} of {ticker}"

    def portfolio_value(self, prices):
        total = self.cash

        for ticker, qty in self.positions.items():
            if ticker in prices:
                total += prices[ticker] * qty

        return total
