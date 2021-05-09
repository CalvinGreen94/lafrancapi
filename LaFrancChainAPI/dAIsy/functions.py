import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import datetime as dt
import cbpro
import time
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split,TimeSeriesSplit


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler as mini
bid_values = np.random.uniform(0.015,0.06,[6000,1])
bid_df = pd.DataFrame(bid_values,columns=['Bid'])
bid =bid_df[-1:]
stake_values = np.random.uniform(0.025,0.032,[6000,1])
stake_df = pd.DataFrame(stake_values,columns=['Stake'])
stake = stake_df[-1:]
clean_values = np.random.uniform(0.015,0.025,[6000,1])
clean_df = pd.DataFrame(clean_values,columns=['Deck1'])
nsfw_values = np.random.uniform(0.026,0.04,[6000,1])  
nsfw_df = pd.DataFrame(nsfw_values,columns=['Deck2']) 
damage1_values = np.random.randint(0,3,[6000,1]) 
damage_df = pd.DataFrame(damage1_values,columns=['Deck1_damage'])
gas_values = np.random.randint(21000,65000,[6000,1]) 
gas_df = pd.DataFrame(gas_values,columns=['gas_values'])
gwei_values = np.random.randint(65,82,[6000,1]) 
gwei_df = pd.DataFrame(gwei_values,columns=['gwei_values'])
gas_price = np.random.uniform(0.000000065,0.000000085,[6000,1]) 
gas_price_df = pd.DataFrame(gas_price,columns=['gas_price_values']) 
player_payout =  np.random.uniform(0.00001278,0.00003195,[6000,1]) 
player_df = pd.DataFrame(player_payout,columns=['player_payout']) 
tx_fee = np.random.uniform(0.00125,0.00228366,[6000,1]) 
tx_df = pd.DataFrame(tx_fee,columns=['tx_fee']) 
damage2_values = np.random.randint(3,7,[6000,1]) 
damage2_df = pd.DataFrame(damage2_values,columns=['Deck2_damage']) 
data = clean_df.join(nsfw_df)
data = data.join(damage_df) 
data = data.join(damage2_df) 
clean_image_no = np.random.randint(0,94,[6000,1]) 
clean_image_df = pd.DataFrame(clean_image_no,columns=['clean_image_no'])
nsfw_image_no = np.random.randint(0,24,[6000,1]) 
nsfw_image_df = pd.DataFrame(nsfw_image_no,columns=['nsfw_image_no']) 
data = data.join(clean_image_df) 
data = data.join(nsfw_image_df)
data=data.join(tx_df) 
data = data.join(player_df) 
data = data.join(gas_df)
data = data.join(gwei_df)
data = data.join(bid_df) 
data = data.join(stake_df)
data = data.to_csv('data/c_force_data.csv',index=False)



def profit_target(token,current_holdings,target_percentage):
    token = token
    print('\n\n {} target'.format(token))
    current_holdings = current_holdings
    target_percentage = current_holdings * .3
    total_target = current_holdings+target_percentage
    print('{} profit target {}, == {}'.format(token,target_percentage,total_target))
    return target_percentage
def loss(token,current_holdings,loss):
    token = token
    print('\n\n {} loss'.format(token))
    current_holdings = current_holdings
    target_percentage = current_holdings * .1
    total_loss = current_holdings-target_percentage
    print('{} stop loss {}, == {}'.format(token,target_percentage,total_loss))
    return target_percentage


def moving_20average(a, n=25) :
    ret = pd.DataFrame.cumsum(a)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def moving_100average(a, n=100) :
    ret = pd.DataFrame.cumsum(a)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

# current_priceetc = current_price('etc-usd')
#
#
# auth_clientetc = current_info['available'][11]
# print('available {}: {}\n\n'.format(current_info['currency'][11],auth_clientetc))
#
#
# currentetc = float(current_priceetc) * float(auth_clientetc)
# print('current etc balance: {}\n\n'.format(currentetc))
#
#
# print('-->PROFIT TARGETS:')
# etc_tar = profit_target('etc',currentetc, .3)
#
# etc_loss = loss('etc',currentetc, .1)

def formatPrice(n):
	return ("-$" if n < 0 else "$") + "{0:.4f}".format(abs(n))
# returns the vector containing stock data from a fixed file

def getStockDataVec(key):
	vec = []
	lines = open("data/" + key + ".csv", "r").read().splitlines()
	print(len(lines))

	for line in lines[48:]:
		vec.append(float(line.split(",")[6])) #GAS
		# print('initializing 20 second moving average')
		# a = moving_20average(vec)
		# print('initializing 100 second moving average')
		# b = moving_100average(vec)
	# for ma in ma20:
	# 	vec.append(float(line.split(',')[4]))
	# for ma1, in ma100:
	# 	vec.append(float(line.split(',')[4]))


	return vec

# returns the sigmoid
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

# returns an an n-day state representation ending at time t
def getState(data, t, n):
	d = t - n + 1
	block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0
	res = []
	for i in range(n - 1):
		res.append(sigmoid(block[i + 1] - block[i]))

	return np.array([res])
