#excercices
class Bond:
    def __init__(self, par_value, coupon_rate, maturity):
        self.par_value = par_value
        self.coupon_rate = coupon_rate
        self.maturity = maturity

    def current_yield(self, market_price):
        return (self.coupon_rate * self.par_value) / market_price

ten_year_note = Bond(1000, 0.025, 10)
yield_on_note = ten_year_note.current_yield(950)
print(yield_on_note)


class Stock:
    def __init__(self , name , price , dividend):
        self.name = name
        self.price = price
        self.dividend = dividend
    

    def yield_dividend(self):
        return self.dividend / self.price
    
apple_stock = Stock('Apple', 150 , 0.82)
print(apple_stock.yield_dividend())

class Portfolio:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.instruments = []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def total_value(self):
        total = 0
        for instrument in self.instruments:
            if isinstance(instrument, Instrument):
                total += instrument.price
        return total

class Instrument:
    def __init__(self, name, price, dividend):
        self.name = name
        self.price = price
        self.dividend = dividend

apple_stock = Instrument('Apple', 150, 0.82)

MR0_portfolio = Portfolio('MR0', 0)
MR0_portfolio.add_instrument(apple_stock)

# Calculate the total value of MR0_portfolio (which currently contains one stock)
total_portfolio_value = MR0_portfolio.total_value()
print(f"Total Portfolio Value for {MR0_portfolio.name}: {total_portfolio_value}")

class CurrencyConverter:
    def __init__(self):
        self.rates = {}

    def add_conversion_rate(self, source_currency, target_currency, rate):
        self.rates[(source_currency, target_currency)] = rate

    def convert(self, amount, source_currency, target_currency):
        # Check if a direct conversion rate exists
        if (source_currency, target_currency) in self.rates:
            return amount * self.rates[(source_currency, target_currency)]
        else:
            # Check if an inverse conversion rate exists
            if (target_currency, source_currency) in self.rates:
                return amount / self.rates[(target_currency, source_currency)]
            else:
                return None 


converter = CurrencyConverter()


converter.add_conversion_rate("USD", "EUR", 0.85)
converter.add_conversion_rate("EUR", "JPY", 125.0)

# Convert 100 USD to EUR
usd_to_eur = converter.convert(100, "USD", "EUR")
print(f"100 USD to EUR: {usd_to_eur} EUR")

# Convert 500 EUR to JPY
eur_to_jpy = converter.convert(500, "EUR", "JPY")
print(f"500 EUR to JPY: {eur_to_jpy} JPY")

class CurrencyConverter:
    def __init__(self):
        # Initialize the conversion rates as a dictionary
        self.rates = {}

    def add_conversion_rate(self, source_currency, target_currency, rate):
        # Add or update the conversion rate in the dictionary
        self.rates[(source_currency, target_currency)] = rate

    def convert(self, amount, source_currency, target_currency):
        # Check if a direct conversion rate exists
        if (source_currency, target_currency) in self.rates:
            return amount * self.rates[(source_currency, target_currency)]
        else:
            # Check if an inverse conversion rate exists
            if (target_currency, source_currency) in self.rates:
                return amount / self.rates[(target_currency, source_currency)]
            else:
                return None  # Conversion rate not found


import numpy as np

np.random.seed(0)  # For reproducibility
daily_returns = np.random.normal(0.001, 0.02, 1000)

stock_prices = [100]

for r in daily_returns:
    new_price = stock_prices[-1] * (1 + r)
    stock_prices.append(new_price)

print(stock_prices[-1])

import numpy as np

# Given values
sigma1 = 0.1  # Standard deviation of asset 1
sigma2 = 0.2  # Standard deviation of asset 2
rho12 = 0.5   # Correlation coefficient between assets 1 and 2
w1 = 0.6      # Weight of asset 1 in the portfolio
w2 = 0.4      # Weight of asset 2 in the portfolio

# Portfolio variance formula
portfolio_variance = (w1 ** 2) * (sigma1 ** 2) + (w2 ** 2) * (sigma2 ** 2) + 2 * w1 * w2 * sigma1 * sigma2 * rho12

print("Portfolio Variance:", portfolio_variance)

import numpy as np

returns = np.array([0.10, 0.15])  #Annual returns
volatilities = np.array([0.20, 0.30])


weights = np.linspace(0, 1, 11)  #eight combinations from 0 to 100% in increments of 10%


portfolio_returns = []
portfolio_volatilities = []


for w in weights:
    portfolio_return = np.dot(returns, [1 - w, w])
    portfolio_volatility = np.sqrt(np.dot(np.dot([1 - w, w], np.diag(volatilities)), [1 - w, w]))
    portfolio_returns.append(portfolio_return)
    portfolio_volatilities.append(portfolio_volatility)


print("Weight\tPortfolio Return\tPortfolio Volatility")
for i in range(len(weights)):
    print(f"{weights[i]:.2f}\t{portfolio_returns[i]*100:.2f}%\t\t{portfolio_volatilities[i]*100:.2f}%")
