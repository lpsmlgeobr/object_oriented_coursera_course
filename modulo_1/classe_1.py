

class Currency(object):
    """Represent Currency Class"""

    def __init__(self, name, symbol, factor):
        self.name = name
        self.symbol = symbol
        self.factor = factor


    def convert_amount_to_base_currency(self, aNumber):
        return aNumber * self.factor

    def convert_amount_from_base_cureency(self, aNumber):
        return aNumber/self.factor

    def __repr__(self):
        return self.name


class Money(object):
    """Represent Money class"""

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def base_currency_amount(self):
        return self.currency.convert_amount_to_base_currency(self.amount)

    def __add__(self, anAmountOfMoney):
        amount = self.base_currency_amount() + anAmountOfMoney.base_currency_amount()
        amount = self.currency.convert_amount_from_base_cureency(amount)
        return Money(amount, self.currency)

    def __sub__(self, anAmountOfMoney):
        amount = self.base_currency_amount() - anAmountOfMoney.base_currency_amount()
        amount = self.currency.convert_amount_from_base_cureency(amount)
        return Money(amount,self.currency)

    def __mul__(self, aNumber):
        return Money(self.amount * aNumber, self.currency)

    def __truediv__(self, aNumber):
        return Money((self.amount / aNumber), self.currency)

    def __repr__(self):
        return "{} {}".format(self.currency.symbol, self.amount)









