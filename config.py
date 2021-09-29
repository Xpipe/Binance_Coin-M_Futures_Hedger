#put in your API KEYS from Binance here
API_KEY = "<<YOUR BINANCE API KEY HERE>>"
SECRET_KEY = "<<YOUR BINANCE SECRET API KEY HERE>>"    

#this variable controls how close the hedge should be to the actual position / when to stop trading / creating new buy / sell orders
#once the delta in btc (between the current open position (hedge) / and the wallet balance of Coin-M futures) is near this value, stop trading
DELTA_AMOUNT_IN_BTC_TO_STOP_TRADING = 0.01 #in BTC terms

#These variables control the amounts / sizes when new orders are placed.  These are ranges - so new orders will randomized be between two values.
PER_ORDER_MIN = 0.01
PER_ORDER_MAX = 0.02

#Symbol to trade - note, this code is designed for BTCUSD_PERP under COIN-M futures, if you try to use it for other symbols, it may break because of decimal order sizes or other issues - if you're interested in other symbols or features, please reach out.
SYMBOL = "BTCUSD_PERP"