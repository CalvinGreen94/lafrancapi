# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/

# Importing the libraries
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
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]'
abi = json.loads(abi)

class DawnFrancBlockchain:

	def __init__(self):
		self.chain = []
		self.transactions = []
		self.create_block(proof = 1, previous_hash = '00000') 
		self.nodes = set()



	def create_block(self, proof, previous_hash):
		block = {'index': len(self.chain) + 1,
				 'timestamp': str(datetime.datetime.now()),
				 'proof': proof,
				 'previous_hash': previous_hash,
				 'transactions': self.transactions }
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
	
	def add_transaction(self,sender,receiver,amount): 
		self.transactions.append({'sender': sender,
		'receiver':receiver,
		'amount':amount})
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
blockchain = DawnFrancBlockchain()
cors = CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:3000/","https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"," https://ropsten.etherscan.io/","http://127.0.0.1:8867/dai_gen","http://127.0.0.1:8867/LaFrancDAI_minted"]}})
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
	new =web3.eth.account.create('') #<-- create mnemonic 
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


# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
	previous_block = blockchain.get_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	DawnFrancBlockchain.add_transaction(sender = node_address , receiver='c1',amount=1)
	block = blockchain.create_block(proof, previous_hash)
	response = {'message': 'Congratulations, you just mined a block!',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
				'previous_hash': block['previous_hash'],
				'transactions': block['transactions']} 
	message = {} 
	data = {}
	message['message'] = 'Congratulations, you just mined  block {} at {}!, Proof of work {}, previous hash {}'.format(block['index'],block['timestamp'],block['proof'],block['previous_hash']) 
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
	json = request.get_json()
	transactions_keys= ['sender','receiver','amount']
	if not all (key in json for key in transactions_keys):
		message['message'] = 'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
		data['status'] =  400
		data['data'] = message   
		return jsonify(data) #'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
	index = blockchain.add_transaction(json['sender'],json['receiver'],json['amount']) 
	response = {'message': f'This Transaction IS NOW ON BLOCK {index}'} 
	message['message'] = f'This Transaction IS NOW ON BLOCK {index}'
	data['status'] = 201 
	data['data'] = message   
	return jsonify(data)

### Decentralizing LaFrancCoin 


###Connecting Nodes 
@app.route('/connect_node', methods = ['POST']) 
def connect_node():
	json = request.get_json() 
	json.get('nodes')
	if nodes is None: 
		response = {'message': f'No Nodes Found'} 

		message['message'] = 'No node connected'
		data['status'] = 400
		data['data'] = message   
		return jsonify(data)

	for node in nodes:
		blockhain.add_node(node)
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






app.run(host = '127.0.0.1', debug=True,port=8685)