from binance.client import Client
import config
import functions
import random
import math
import string

'''
This script controls the main logic of mananging the hedge / position.
'''

#initialize / connect to the Binance API with the specified keys
client = Client(config.API_KEY, config.SECRET_KEY, testnet=False)

delivery_account_informations = client.futures_coin_account()

user = {}
for asset in delivery_account_informations['assets']:
    if asset['asset'] == 'BTC':
        user['futures_wallet_amount_BTC'] = asset

for position in delivery_account_informations['positions']:
    if position['symbol'] == 'BTCUSD_PERP':
        user['futures_current_position'] = position

#calculate difference / delta in the wallet vs. position
delta_wallet_position_amt = float(user['futures_wallet_amount_BTC']['walletBalance']) - (abs(float(user['futures_current_position']['notionalValue'])) - abs(float(user['futures_wallet_amount_BTC']['unrealizedProfit'])))
abs_delta_wallet_position_amt = abs(delta_wallet_position_amt)

print('Delta btwn Wallet / Position Amt = ' + str(delta_wallet_position_amt) + '\n')

#which one is larger?  wallet or notionalValue (-profLoss)
if abs_delta_wallet_position_amt < config.DELTA_AMOUNT_IN_BTC_TO_STOP_TRADING:
	exit('WalletBalance / OpenPosition are very close to : ' + str(abs_delta_wallet_position_amt) + ' BTC - stopping trading\n')
elif float(user['futures_wallet_amount_BTC']['walletBalance']) > (abs(float(user['futures_current_position']['notionalValue'])) - abs(float(user['futures_wallet_amount_BTC']['unrealizedProfit']))):
	print('WalletBalance is larger by ' + str(abs_delta_wallet_position_amt) + ' BTC so I have to short more.\n')
	direction_to_go = "SELL"
else:
	print('NotionalValue +/- ProfLoss is Larger by ' + str(abs_delta_wallet_position_amt) + ' BTC so I have to buy / cover.\n')
	direction_to_go = "BUY"

instrument_name = config.SYMBOL

ticker = client.futures_coin_orderbook_ticker(symbol=instrument_name)
ticker = ticker[0]

#set the max / min values based on the delta btc amt
max_trade_size = config.PER_ORDER_MAX
min_trade_size = config.PER_ORDER_MIN

amount_in_btc = random.randint(min_trade_size * 100, max_trade_size * 100) / 100 #number of COIN for buy / sell

#if the open position is close to the wallet balance, the next order amount submitted doesn't cause the open position to go beyond the delta - aka it adjusts the new orders to help get close to the wallet balance and create a perfect hedge and eventually stop the script from submitting new orders
if amount_in_btc > abs_delta_wallet_position_amt:
	min_trade_size = 0.01
	max_trade_size = abs_delta_wallet_position_amt
	amount_in_btc = round(random.uniform(min_trade_size * 100, max_trade_size * 100) / 100, 8) #number of COIN for buy / sell

amount_in_USD = amount_in_btc * float(ticker['bidPrice'])
amount = round((amount_in_btc * float(ticker['bidPrice'])) / 100)

#convert the $amount into BTC amount
print('\nmax_trade_size: ' + str(max_trade_size) + '\n\
min_trade_size: ' + str(min_trade_size) + '\n\
Amount in BTC: ' + str(amount_in_btc) + '\n\
Amount in USD: ' + str(amount_in_USD) + '\n\
Ticker: ' + ticker['bidPrice'] + '\n\
Amount in Contracts: ' + str(amount) + '\n\
Direction to go: ' + direction_to_go + '\n')

cancel = False
current_openOrder_price = 0
		
openPositions = client.futures_coin_position_information()

btc_position = []
for openPosition in openPositions:
    if openPosition['symbol'] == instrument_name:
        btc_position.append(openPosition)

temp_openOrders = client.futures_coin_get_open_orders(symbol=instrument_name)

openOrders = []
for openOrder in temp_openOrders:
	if openOrder['type'] == "LIMIT":
		openOrders.append(openOrder)

if len(openOrders) > 1:
	orderC = client.futures_coin_cancel_all_open_orders(symbol=instrument_name)
	cancel = True
elif len(openOrders) == 1:
	current_openOrder_price = openOrders[0]['price']
	if direction_to_go == 'BUY' and current_openOrder_price == ticker['bidPrice']:
		cancel = False
	elif direction_to_go == 'SELL' and current_openOrder_price == ticker['askPrice']:
		cancel = False	
	else:
		orderC = client.futures_coin_cancel_all_open_orders(symbol=instrument_name)
		cancel = True

rand_string = functions.random_strings(17)
newClientOrderId = 'HEDGER-MC-' + rand_string
#string | user defined label for the order (maximum 32 characters)

if direction_to_go == 'BUY':
	if cancel == True or (current_openOrder_price != ticker['bidPrice']):
		print('bid: ' + ticker['bidPrice'] + '\n')
		print('Amount: ' + str(amount) + '\n')
		
		price = ticker['bidPrice']
		while 1 == 1:
			order = client.futures_coin_create_order(side='BUY',symbol=instrument_name,quantity=amount,price=price,type='LIMIT',newClientOrderId=newClientOrderId,timeInForce='GTX',recvWindow=60000)
			print(order)
				
			if order['status'] != 'NEW':
				price -= 0.50

				order = client.futures_coin_create_order(side='BUY',symbol=instrument_name,quantity=amount,price=price,type='LIMIT',newClientOrderId=newClientOrderId,timeInForce='GTX',recvWindow=60000)
				print(order)
				
				price -= 0.50
			else:
				break
			exit()			
	else:
		print('Current Order Price = Current bid Price\n')

elif direction_to_go == 'SELL':
	if cancel == True or (current_openOrder_price != ticker['askPrice']):
		print('ask: ' + ticker['askPrice'] + '\n')
		print('Amount: ' + str(amount) + '\n')
		
		price = ticker['askPrice']
		while 1 == 1:						
			order = client.futures_coin_create_order(side='SELL',symbol=instrument_name,quantity=amount,price=price,type='LIMIT',newClientOrderId=newClientOrderId,timeInForce='GTX',recvWindow=60000)
			print(order)

			if order['status'] != 'NEW':
				price += 0.50

				order = client.futures_coin_create_order(side='SELL',symbol=instrument_name,quantity=amount,price=price,type='LIMIT',newClientOrderId=newClientOrderId,timeInForce='GTX',recvWindow=60000)
				print(order)
				
				price += 0.50
			else:
				break
			exit()
	else:
		print('Current Order Price = Current ask Price\n')