from zipline.api import order, record, symbol, set_benchmark, sid

def initialize(context):
    set_benchmark(symbol('BTC_USD'))

def handle_data(context, data):
    print("handle_data {}".format(data.current(symbol('BTC_USD'), 'price')))
    print("handle_data {}".format(data.current(symbol('ETH_USD'), 'price')))
    print("handle_data {}".format(data.current(symbol('XRP_USD'), 'price')))
    order(symbol('BTC_USD'), 10)
    record(BTC_USD=data.current(symbol('BTC_USD'), 'price'))
