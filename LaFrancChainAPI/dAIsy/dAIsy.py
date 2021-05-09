from agent2.agent import Agent
from functions import *
import sys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import hashlib
import json
from flask import Flask, jsonify
from flask import Flask, jsonify,request 
from urllib.parse import urlparse  
from uuid import uuid4
from flask_cors import CORS
# Part 1 - Building a Blockchain
from web3 import Web3 
from web3 import middleware
from web3.middleware import geth_poa_middleware
infura_url = "https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"
web3 = Web3(Web3.HTTPProvider(infura_url))
from web3.middleware import geth_poa_middleware
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
abi = json.loads(abi)
address1 = '0xAb0Bf4038340fd8d77921B28b7A5Fb574B5ECCa6'
dai = web3.eth.contract(address=address1, abi=abi)   
w3 = Web3()
import os
import csv
import datetime
import tensorflow as tf 
os.environ['KERAS_BACKEND' ] = 'tensorflow'
os.environ['MKL_THREADING_LAYER'] = 'GNU'
w3.middleware_onion.add(middleware.time_based_cache_middleware)
w3.middleware_onion.add(middleware.simple_cache_middleware)
daisy = 'dAIsy'
from matplotlib import style
import pandas as pd
if len(sys.argv) != 4:
	print("Usage: python train.py [stock] [window] [episodes]")
	exit()
stock_name, window_size, episode_count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
agent = Agent(window_size)
data = getStockDataVec(stock_name)
l = len(data) - 1
batch_size = 710

import json
from web3.middleware import geth_poa_middleware



mint_acct ='0xa71403F82127830fB739E622Cf829D120593FD7F'
mint_key = '28847b758011bae3697701a27bf89d59920327e7bdabd44fb5e02d7cdeb1612d'
web3.eth.mint_acct = mint_acct
receiver1= '0x7E5453ef00e59EA57c5fDDb5d10ad7eBebD6B66b'

web3.eth.receiver1 = receiver1
new =web3.eth.account.create('You Come t0 m3 0n th3 dai 0f mah dAUghterZZzz wedDinng')
new_add =  new._address
new_key = new.key    
web3.eth.miner = mint_acct
class LaFrancBlockchain:

	def __init__(self):
		self.chain = []
		self.transactions = []
		self.create_block(proof = 1, previous_hash = '00000') 
		self.nodes = set()
	def create_block(self, proof, previous_hash):
		address = '0xAb0Bf4038340fd8d77921B28b7A5Fb574B5ECCa6'
		abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
		dai = web3.eth.contract(address=address, abi=abi)		
		mint_acct ='0xa71403F82127830fB739E622Cf829D120593FD7F'
		mint_key = '28847b758011bae3697701a27bf89d59920327e7bdabd44fb5e02d7cdeb1612d'    
		web3.eth.mint_acct = mint_acct
		receiver1= '0x240bb9A0F96898E4bba2105b3A06E02244f3965D'

		block = {'index': len(self.chain) + 1,
				 'timestamp': str(datetime.datetime.now()),
				 'proof': proof,
				 'previous_hash': previous_hash,
				 'transactions': self.transactions,
				 'Miner_Minting_Address':mint_acct, 
                 'receiver':receiver1 
				 }
		self.transactions = []	 
		self.chain.append(block) 
		return block 

	def get_previous_block(self):
		return self.chain[-1]

	def proof_of_work(self, previous_proof):
		new_proof = 1
		check_proof = False
		while check_proof is False:
			hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
			if hash_operation[:4] == '0000':
				check_proof = True
			else:
				new_proof += 1
		return new_proof
	
	def hash(self, block):
		encoded_block = json.dumps(block, sort_keys = True).encode()
		return hashlib.sha256(encoded_block).hexdigest()
	
	def is_chain_valid(self, chain):
		previous_block = chain[0]
		block_index = 1
		while block_index < len(chain):
			block = chain[block_index]
			if block['previous_hash'] != self.hash(previous_block):
				return False
			previous_proof = previous_block['proof']
			proof = block['proof']
			hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
			if hash_operation[:4] != '0000':
				return False
			previous_block = block
			block_index += 1
		return True
	
	def add_transaction(self,sender,receiver,amount): # sender = sender receiver = receiver amount = amount
		address = '0xAb0Bf4038340fd8d77921B28b7A5Fb574B5ECCa6'
		abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
		dai = web3.eth.contract(address=address, abi=abi)		
		mint_acct ='0xa71403F82127830fB739E622Cf829D120593FD7F'
		mint_key = '28847b758011bae3697701a27bf89d59920327e7bdabd44fb5e02d7cdeb1612d'    
		receiver1= '0x7E5453ef00e59EA57c5fDDb5d10ad7eBebD6B66b'

		previous_block = blockchain.get_previous_block()
		previous_proof = previous_block['proof']
		proof = blockchain.proof_of_work(previous_proof)
		previous_hash = blockchain.hash(previous_block)     
		self.transactions.append({'sender': sender,
		'receiver':receiver1,
		'amount':amount,
		'minter':mint_acct})
		previous_block = self.get_previous_block()
		return previous_block['index'] + 1 

	def add_node(self, address):
		# address = 'http:127.0.0.1:8677/'
		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc) 
		# node = parsed_url.															   
#Give the Chain a Reason to exist 
	def replace_chain(self): 
		network = self.nodes 
		longest_chain = None 
		max_length = len(self.chain)
		for node in network:
			response = requests.get(f'http://{node}/get_chain') 
			if response.status_code == 200:
				length = response.json()['length'] 
				chain = response.json()['chain'] 
				if length > max_length and self.is_chain_valid(chain):
					max_length = length 
					longest_chain = chain 
		if longest_chain:
			self.chain = longest_chain
			return True 
		return False 

app = Flask(__name__)
#Creating Addresses for nodes on Port:8677
node_address = str(uuid4()).replace('-','')

# Creating a Blockchain
blockchain = LaFrancBlockchain()
# cors = CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:3000/","https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"," https://ropsten.etherscan.io/","http://127.0.0.1:8867/dai_gen","http://127.0.0.1:8867/LaFrancDAI_minted"]}})

for e in range(episode_count + 1):
	print("Episode " + str(e) + "/" + str(episode_count))
	state = getState(data, 0, window_size + 1)
	total_profit = 0
	agent.inventory = []
	starting_balance = dai.functions.balanceOf(mint_acct).call()
	print('starting balance {}'.format(starting_balance))
	# buying_power = 6#if price <= $5.21

	for t in range(l):
		action = agent.act(state)
		# hold
		next_state = getState(data, t + 1, window_size + 1)
		reward = 1.
		#buy
		if action == 1 :
			agent.inventory.append(data[t])
			print('Current Balance {}'.format(dai.functions.balanceOf(mint_acct).call()))
			
			address = '0xAb0Bf4038340fd8d77921B28b7A5Fb574B5ECCa6'
			abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
			dai = web3.eth.contract(address=address, abi=abi)		
			mint_acct ='0xa71403F82127830fB739E622Cf829D120593FD7F'
			mint_key = '28847b758011bae3697701a27bf89d59920327e7bdabd44fb5e02d7cdeb1612d'    
			previous_block = blockchain.get_previous_block()
			previous_proof = previous_block['proof']
			proof = blockchain.proof_of_work(previous_proof)
			previous_hash = blockchain.hash(previous_block)
			web3.eth.mint_acct = mint_acct
			receiver1= '0x7E5453ef00e59EA57c5fDDb5d10ad7eBebD6B66b'
			amount =  web3.toWei(float(.003),'ether')
			# mint_tx =dai.functions.transfer(mint_acct, 0x00000000000000).buildTransaction({'chainId': 3, 'gas':7000000, 'nonce':  web3.eth.getTransactionCount(mint_acct)})
			# signed_tx = web3.eth.account.signTransaction(mint_tx, mint_key)
			# tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			# mint_tx =dai.functions.transfer(mint_acct,  0x00000000000000).buildTransaction({'chainId': 3, 'gas':270000, 'nonce':  web3.eth.getTransactionCount(mint_acct)})
			# signed_tx = web3.eth.account.signTransaction(mint_tx, mint_key)
			# tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			mint_tx =dai.functions.transfer(receiver1,0x70000009999999).buildTransaction({'chainId': 3, 'gas':8000000, 'nonce':  web3.eth.getTransactionCount(mint_acct)*1000000})
			signed_tx = web3.eth.account.signTransaction(mint_tx, mint_key)
			tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			blockchain.add_transaction(sender = mint_acct , receiver=receiver1,amount=amount)
			block = blockchain.create_block(proof, previous_hash)
			response = {'message': 'Congratulations, you just mined a block!',
						'index': block['index'],
						'timestamp': block['timestamp'],
						'proof': block['proof'],
						'previous_hash': block['previous_hash'],
						'ETHEREUM_HASH': tx_hash,
						'transactions': block['transactions'],
						'receiver':receiver1} 
			print(response)
			response = {'chain': blockchain.chain,
				'length': len(blockchain.chain)}
			print(response)
			is_valid = blockchain.is_chain_valid(blockchain.chain)
			if is_valid:
				response = {'message': 'All good. The Blockchain is valid.'}	

				print(response) 
			else:
				response = {'message': 'Houston, we have a problemo. The Blockchain is not valid.'} 
				print(response)
			@app.route('/add_transaction', methods = ['POST'])
			def add_transaction():
				json = request.get_json()

				transactions_keys= ['sender','receiver','amount'] 

				if not all (key in json for key in transactions_keys):
					response = {'message':  'HOME ELMENTS OF THE TRASACTION ARE MISSING'}
					message['message'] = 'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
					data['status'] =  400
					data['data'] = message   
					return(jsonify(data)) #'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
				index = blockchain.add_transaction(json['sender'],json['receiver'],json['amount']) 
				response = {'message': f'This Transaction IS NOW ON BLOCK {index}'} 
				return jsonify(response)



		# sell
		elif action == 2 and len(agent.inventory) > 0:
			import json
			from web3.middleware import geth_poa_middleware
			infura_url = "https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"
			web3 = Web3(Web3.HTTPProvider(infura_url))
			web3.middleware_onion.inject(geth_poa_middleware, layer=0)
			abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"sender","type":"address"},{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"value","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"name","type":"string"},{"name":"symbol","type":"string"},{"name":"decimals","type":"uint8"},{"name":"totalSupply","type":"uint256"},{"name":"feeReceiver","type":"address"},{"name":"tokenOwnerAddress","type":"address"}],"payable":true,"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'
			abi = json.loads(abi)
			is_chain_replaced = blockchain.replace_chain()
			message = {} 
			data = {}
			if is_chain_replaced:
				response = {'message': 'NODES HAD DIFFERENT CHAINS , REPLACED BY LONGEST CHAIN',
				'new_chain': blockchain.chain }
				message['message'] = 'NODES HAD DIFFERENT CHAINS , REPLACED BY LONGEST CHAIN {}'.format(blockchain.chain)
				data['status'] = 200 
				data['data'] = message
			else:
				response = {'message': 'NODE IS CONNECT TO LARGEST CHAIN',
				'actual_chain':blockchain.chain}
				message['message'] = 'NODE IS CONNECT TO LARGEST CHAIN {}'.format(blockchain.chain)
				data['status'] = 200 
				data['data'] = message   
			print(response)



		###Connecting Nodes 
		@app.route('/connect_node', methods = ['POST']) 
		def connect_node():
			message = {} 
			data = {}   
			json = request.get_json() 
			nodes = json.get('nodes')
			if nodes is None: 
				response = {'message': f'No Nodes Found'} 

				message['message'] = 'No node connected'
				data['status'] = 400
				data['data'] = message   
				print(response)

			for node in nodes:
				blockchain.add_node(node)
			response = {'message':'THE FOLLOWING NODES ARE CONNECTED',
			'total_nodes': list(blockchain.nodes)} 
			message['message'] = 'THE FOLLOWING NODES ARE CONNECTED {}'.format(list(blockchain.nodes))
			data['status'] = 201 
			data['data'] = message   
			print(response)



		# a2 = pd.to_csv('SellPrice.csv')
		done = True if t == l - 1 else False
		agent.memory.append((state, action, reward, next_state, done))

		state = next_state
		s = pd.DataFrame(state)
		s = s.to_csv('state.csv')
		if done:
			print("--------------------------------")
			# print("Current info: ")
			print("--------------------------------")
			print('Current Balance {}'.format(dai.functions.balanceOf(mint_acct).call()))

		if len(agent.memory) > batch_size:
			agent.expReplay(batch_size)

	if e % 10 == 0:
		log_dir = "models/agent3/logs/" #+ datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
		tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
		agent.model.save("models/agent3/model_ep-" + str(e))
app.run(host = '127.0.0.1', debug=True,port=8678)