# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
#INSOMNIA HTTP CLIENT 
# Importing the libraries
import datetime
import hashlibfrom tronpy import Tron,Contract
from tronpy.keys import PrivateKey
import datetime
import hashlib
import json
import os
from flask import Flask, jsonify,redirect 
from flask import Flask, jsonify,request, render_template
import re 
from urllib.parse import urlparse  
from uuid import uuid4
from flask_cors import CORS
# Part 1 - Building a Blockchain
from web3 import Web3 
from web3 import middleware
from web3.middleware import geth_poa_middleware
client1 = Tron()
import numpy as np
from flask import send_file
from flask import Flask, session,abort,request, jsonify, render_template,redirect,url_for,flash,redirect
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler as mini
import wolframalpha
import wikipedia
import os
import stripe
import datetime
import subprocess
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import webbrowser
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from espeakng import ESpeakNG 
import wave 
# import pyaudio 
# import StringIO
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
daisy = 'dAIsy'
app = Flask(__name__)
app.secret_key = "You Come t0 m3 0n th3 dai 0f mah dAUghterZZzz wedDinng BITCH!"
pub_key ='pk_live_2pO0yUvt9xKyjAo9rca8Vkc600FWtgJuqZ'


class LaFrancBlockchain:

	def __init__(self):
		self.chain = []
		self.transactions = []
		self.create_block(proof = 1, previous_hash = '00000') 
		self.nodes = set()



	def create_block(self, proof, previous_hash):
		import bs4
		import urllib.request
		import requests
		from urllib.request import urlopen
		from bs4 import BeautifulSoup as soup
		import random
		my_url = 'http://lafranccoinbase.herokuapp.com/sakujoooCloud/'
		#opening up connection, downloading the page
		html_page = requests.get('http://lafranccoinbase.herokuapp.com/sakujoooCloud/')
		soup = soup(html_page.content, 'html.parser')
		warning = soup.find('div', class_="lister-item mode-detail")
		images = warning.findAll('img')
		image = images
		image = str('http://lafranccoinbase.herokuapp.com/sakujoooCloud/{}'.format(image[0:]))
		command = takeCommand()

		mint_acct ='' #<= input acct address 
		mint_key = '' #<= input acct priv. key	
		receiver1= ''
		
		block = {'index': len(self.chain) + 1,
				 'timestamp': str(datetime.datetime.now()),
				 'proof': proof,
				 'previous_hash': previous_hash,
				 'transactions': self.transactions,
				 'Miner_Minting_Address':mint_acct, 
				   'receiver':receiver1 ,
				   'image':image,
				   'totalSupply':cntr.functions.max_yappolacoins(),
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
		mint_acct =''
		priv_key = PrivateKey(bytes.fromhex(""))
		# web3.eth.mint_acct = mint_acct
		receiver1= ''


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


		   





# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)
#Creating Addresses for nodes on Port:8677
node_address = str(uuid4()).replace('-','')


# Creating a Blockchain
blockchain = LaFrancBlockchain()
cors = CORS(app, resources={r"/*": {"origins": ["http://lafranccoinbase.herokuapp.com/sakujoooCloud/","http://127.0.0.1:3000/","http://localhost:8000/api/","https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"," https://ropsten.etherscan.io/","http://127.0.0.1:8678/dai_gen","http://127.0.0.1:8678/yappolaDAI_minted"]}})
# cors = CORS(infura_url, resources={r"/*": {"origins": "https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"}})

@app.route('/home')
def home():
	message = {}
	data = {}

	message['message'] = 'Welcome To The Official LaFranc Decentralized Network !'
	data['status'] = 200
	data['data'] = message

	return jsonify(data)
@app.route('/dai_gen')
def dai_gen():
	from tronpy import Tron
	from tronpy.keys import PrivateKey

	client = Tron() 
	node = client.get_node_info()
	new_cl = client.generate_address()

	warning = 'COPY/PASTE User Address / PRIVATE KEY-> Address: base58check_address, PRIVATE KEY: private_key'

	message = {}
	add = {}
	data = {}

	message['message'] = 'NODE :"{}":   New Address/Private key. Use This To get paid for image uploads. ["({})"], [{}]'.format(node,new_cl,warning)
	add['address'] = str(new_cl)
	data['status'] = 200
	data['data'] = message

	return jsonify(data)
import json
from flask import Flask, request, jsonify


# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
	client = Tron() 
	client1 = Tron(network='nile')
	amount =  1
	mint_acct =''
	priv_key = PrivateKey(bytes.fromhex(""))
	receiver1= ''
	previous_block = blockchain.get_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	# amount =  web3.toWei(float(.0003),'ether')

	txn = (client.trx.transfer(mint_acct,receiver1, 1)
				.memo("did it work")
				.build()
				.sign(priv_key)
		)
	tx_hash = txn.txid
	# tx_hash = hash(tx_hash)+hash(tx_hash)**2
	txn.broadcast()	blockchain.add_transaction(sender = mint_acct , receiver=receiver1,amount=amount)
	block = blockchain.create_block(proof, previous_hash)
	response = {'message': 'Congratulations, you just mined a block!',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
				'previous_hash': block['previous_hash'],
				'LFR-TRX_HASH': tx_hash,
				'transactions': block['transactions'],
				'receiver':receiver1,
				'image':block['image']} 
	message = {} 
	data = {}
	message['message'] = 'Congratulations, you just mined  block {} at {}!, \n LaFranc-TRX HASH {}, Proof of work {}, previous LaFranc hash {}, \n transactions{}, \n RECEIVING MINTER {}'.format(block['index'],block['timestamp'],web3.toHex(tx_hash),block['proof'],block['previous_hash'],block['transactions'],receiver1) 
	data['status']= 200
   
	data['data'] = message
	data1 = pd.DataFrame(data['data'])
	return data1

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
	response = {'chain': blockchain.chain,
				'length': len(blockchain.chain)}
	message = {}
	data = {}
	message['message'] = ' length {}, \n full blockchain {}'.format(len(blockchain.chain),blockchain.chain)
	data['status']= 200
   
	data['data'] = message
	return data

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
	is_valid = blockchain.is_chain_valid(blockchain.chain)
	message = {} 
	data = {}
	if is_valid:
		response = {'message': 'All good. The Blockchain is valid.'}
		message['message'] = 'All good,Blockchain Is Valid' 
		data['status'] = 200 
		data['data'] = message
	else:
		response = {'message': 'Houston, we have a problemo. The Blockchain is not valid.'}
		message['message'] = 'Houston, we have a problemo. The Blockchain is not valid' 
		data['status'] = 200 
		data['data'] = message   
	return jsonify(data)

### Adding LaFrancChain Transactions
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
	message = {} 
	data = {}
	json = request.get_json()
	transactions_keys= ['sender','receiver','amount']
	if not all (key in json for key in transactions_keys):
		message['message'] = 'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
		data['status'] =  400
		data['data'] = message   
		return jsonify(data) #'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
	index = blockchain.add_transaction(json['sender'],json['receiver'],json['amount']) 
	response = {'message': f'This Transaction IS NOW ON BLOCK {index}'}
	message['message'] = 'This Transaction IS NOW ON BLOCK {}'.format(index)
	data['status'] = 201 
	data['data'] = message   
	return jsonify(response),201

### Decentralizing LaFrancCoin 


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
		return jsonify(data)

	for node in nodes:
		blockchain.add_node(node)
	response = {'message':'THE FOLLOWING NODES ARE CONNECTED',
	'total_nodes': list(blockchain.nodes)} 
	message['message'] = 'THE FOLLOWING NODES ARE CONNECTED {}'.format(list(blockchain.nodes))
	data['status'] = 201 
	data['data'] = message   
	return jsonify(data)


### Connect longest chain if necessary
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
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
	return jsonify(data)

from bs4 import BeautifulSoup



import requests

import urllib.request

import shutil





usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}



if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.run(host = '127.0.0.1', debug=True,port=8686)

import json
import os
from flask import Flask, jsonify,redirect 
from flask import Flask, jsonify,request, render_template
import re 
from urllib.parse import urlparse  
from uuid import uuid4
from flask_cors import CORS
# Part 1 - Building a Blockchain
from web3 import Web3 
from web3 import middleware
from web3.middleware import geth_poa_middleware
infura_url = "https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"
web3 = Web3(Web3.HTTPProvider(infura_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
abi = json.loads(abi)

class LaFrancBlockchain:

	def __init__(self):
		self.chain = []
		self.transactions = []
		self.create_block(proof = 1, previous_hash = '00000') 
		self.nodes = set()



	def create_block(self, proof, previous_hash):
		import bs4
		import urllib.request
		import requests
		from urllib.request import urlopen
		from bs4 import BeautifulSoup as soup
		import random
		my_url = 'http://127.0.0.1:8000/sakujoooCloud/'
		#opening up connection, downloading the page
		html_page = requests.get('http://127.0.0.1:8000/sakujoooCloud/')
		soup = soup(html_page.content, 'html.parser')
		warning = soup.find('div', class_="lister-item mode-detail")
		images = warning.findAll('img')
		image = images
		image = str('http://127.0.0.1:8000/sakujoooCloud/{}'.format(image[0:]))

		
		address = '0xAb0Bf4038340fd8d77921B28b7A5Fb574B5ECCa6'
		abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
		dai = web3.eth.contract(address=address, abi=abi)		
		mint_acct ='' #<= input acct address 
		mint_key = '' #<= input acct priv. key	
		web3.eth.mint_acct = mint_acct
		receiver1= '0x240bb9A0F96898E4bba2105b3A06E02244f3965D'
		
		block = {'index': len(self.chain) + 1,
				 'timestamp': str(datetime.datetime.now()),
				 'proof': proof,
				 'previous_hash': previous_hash,
				 'transactions': self.transactions,
				 'Miner_Minting_Address':mint_acct, 
				   'receiver':receiver1 ,
				   'image':image
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
		mint_acct ='' #<= input acct address 
		mint_key = '' #<= input acct priv. key
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


		   





# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)
#Creating Addresses for nodes on Port:8677
node_address = str(uuid4()).replace('-','')


# Creating a Blockchain
blockchain = LaFrancBlockchain()
cors = CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:3000/","http://localhost:8000/api/","https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"," https://ropsten.etherscan.io/","http://127.0.0.1:8686/dai_gen","http://127.0.0.1:8686/LaFrancDAI_minted"]}})
# cors = CORS(infura_url, resources={r"/*": {"origins": "https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"}})

@app.route('/home')
def home():
	message = {}
	data = {}

	message['message'] = 'Welcome To The Official LaFranc Decentralized Network !'
	data['status'] = 200
	data['data'] = message

	return jsonify(data)
@app.route('/dai_gen')
def dai_gen():
	address = '0x47edc4747A04e968AdfCEefE97af25a61b5B9A9C'
	dai = web3.eth.contract(address=address, abi=abi)		
	mint_acct ='' #<= input acct address 
	mint_key = '' #<= input acct priv. key
	web3.eth.mint_acct = mint_acct
	new =web3.eth.account.create('You Come t0 m3 0n th3 dai 0f mah dAUghterZZzz wedDinng')
	new_add =  new._address
	new_key = new.key	

	message = {}
	add = {}
	data = {}

	message['message'] = 'New LaFranc-Dai Address {}, Private key {} mnemonic PLEASE SAVE THIS Information and don"t share with anyone: .LaFranc-DAI left in supply.  BURNER ADDRESS: , the Address is now available on the Ethereum network.  LFR has been generated into your new wallet , thank you for contributing'.format(str(new_add),web3.toHex(new_key))
	add['address'] = str(new_add)
	data['status'] = 200
	data['data'] = message

	return jsonify(data)
import json
from flask import Flask, request, jsonify


# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
	address = '0xAb0Bf4038340fd8d77921B28b7A5Fb574B5ECCa6'
	abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
	dai = web3.eth.contract(address=address, abi=abi)		
	mint_acct ='' #<= input acct address 
	mint_key = '' #<= input acct priv. key
	previous_block = blockchain.get_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	web3.eth.mint_acct = mint_acct
	receiver1= '0x7E5453ef00e59EA57c5fDDb5d10ad7eBebD6B66b'
	amount =  web3.toWei(float(.003),'ether')
	# mint_tx =dai.functions.transfer(mint_acct, 0x00000000000000).buildTransaction({'chainId': 3, 'gas':8000000, 'nonce':  web3.eth.getTransactionCount(mint_acct)})
	# signed_tx = web3.eth.account.signTransaction(mint_tx, mint_key)
	# tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	# mint_tx =dai.functions.transfer(mint_acct,  0x00000000000000).buildTransaction({'chainId': 3, 'gas':8000000, 'nonce':  web3.eth.getTransactionCount(mint_acct)+1})
	# signed_tx = web3.eth.account.signTransaction(mint_tx, mint_key)
	# tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	mint_tx =dai.functions.transfer(receiver1, 0x00000053999999).buildTransaction({'chainId': 3, 'gas':8000000, 'nonce':  web3.eth.getTransactionCount(mint_acct)+1})
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
				'receiver':receiver1,
				'image':block['image']} 
	message = {} 
	data = {}
	message['message'] = 'Congratulations, you just mined  block {} at {} , \n ETHEREUM HASH {}, Proof of work {}, previous LAFRANC hash {}, \n transactions{}, \n RECEIVING MINTER {}, Containing these images {}!'.format(block['index'],block['timestamp'],web3.toHex(tx_hash),block['proof'],block['previous_hash'],block['transactions'],receiver1,block['image']) 
	data['status']= 200
   
	data['data'] = message
	return jsonify(data)


# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
	response = {'chain': blockchain.chain,
				'length': len(blockchain.chain)}
	message = {}
	data = {}
	message['message'] = ' length {}, \n full blockchain {}'.format(len(blockchain.chain),blockchain.chain)
	data['status']= 200
   
	data['data'] = message
	return data

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
	is_valid = blockchain.is_chain_valid(blockchain.chain)
	message = {} 
	data = {}
	if is_valid:
		response = {'message': 'All good. The Blockchain is valid.'}
		message['message'] = 'All good,Blockchain Is Valid' 
		data['status'] = 200 
		data['data'] = message
	else:
		response = {'message': 'Houston, we have a problemo. The Blockchain is not valid.'}
		message['message'] = 'Houston, we have a problemo. The Blockchain is not valid' 
		data['status'] = 200 
		data['data'] = message   
	return jsonify(data)

### Adding LaFrancChain Transactions
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
	message = {} 
	data = {}
	json = request.get_json()
	transactions_keys= ['sender','receiver','amount']
	if not all (key in json for key in transactions_keys):
		message['message'] = 'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
		data['status'] =  400
		data['data'] = message   
		return jsonify(data) #'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
	index = blockchain.add_transaction(json['sender'],json['receiver'],json['amount']) 
	response = {'message': f'This Transaction IS NOW ON BLOCK {index}'}
	message['message'] = 'This Transaction IS NOW ON BLOCK {}'.format(index)
	data['status'] = 201 
	data['data'] = message   
	return jsonify(response),201

### Decentralizing LaFrancCoin 


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
		return jsonify(data)

	for node in nodes:
		blockchain.add_node(node)
	response = {'message':'THE FOLLOWING NODES ARE CONNECTED',
	'total_nodes': list(blockchain.nodes)} 
	message['message'] = 'THE FOLLOWING NODES ARE CONNECTED {}'.format(list(blockchain.nodes))
	data['status'] = 201 
	data['data'] = message   
	return jsonify(data)


### Connect longest chain if necessary
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
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
	return jsonify(data)

from bs4 import BeautifulSoup



import requests

import urllib.request

import shutil



url = "http://127.0.0.1:8000/sakujoooCloud"


usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}



if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.run(host = '127.0.0.1', debug=True,port=8686)
