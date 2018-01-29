from zipline.api import order, symbol, set_benchmark
from zipline.finance import commission

stocks = ['BTC_USD']


def initialize(context):
    set_benchmark(symbol('BTC_USD'))
    context.set_commission(commission.PerDollar(cost=0.002))
    context.has_ordered = False
    context.stocks = stocks


def handle_data(context, data):
    if not context.has_ordered:
        for stock in context.stocks:
            order(symbol(stock), 100.2)
        context.has_ordered = True