python --version >=3.6 or <= 3.8
Vue.js/Nuxt.js<br /><br /> -Implementation of JWT available while using the infura node for web3 transactions.
<br /><br /><br /><br />
-- Necessary Python imports:
### pip install flask, flask_cors, web3 <br /><br /><br /><br />

<h1>>Make Sure Ports are valid above port 8685 via Flask</h1>

<h3> LaFrancCoin ports 8676-8677 are currently used as the hosting nodes. please feel free to use any ports existing after 8685
</h3>
<br /> <br />

<h4>DO NOT CHANGE RECEIVER1 ADDRESS !!! THIS IS HOW MINERS GAIN MINING REWARDS/LIQUIDITY <br>
 <p>:) <3 <(^^^)> </h4></p> <br />
<br />
<h3>BACKEND</h3>
<h7>PYTHON</h7>


<p>Routing </p> <br /><br />

: Route-> create_block:<h4>-Provides Logic for the existing blockchain:</h4>
mint_acct ='' <- Must generate an address<br />
mint_key = '' <- Generate key for address<br />

: Route-> get_previous_block: <h4>-Receives information from previous block on current node</h4> <br /><br /><br />


: Route-> proof_of_work: <h4>-Initial LaFranc Protocol for how the chain will implement mining</h4>
 <br /><br /><br />


: Route-> hash: <h4>-Hashing operation for keeping information secure during transactions via sha256 addresses</h4><br /><br /><br />


: Route-> is_chain_valid: <h4>-Ensures validity of chain length as well as making sure the nodes are connected to the correct chain</h4><br /><br /><br />


: Route-> add_transaction: <h4>-Adds most recent transactions to the current block on the blockchain
</h4> <br /><br /><br />


: Route-> add_node: <h4>-BACKEND TO ENSURE NODE IS CONNECTED TO THE NETWORK VIA POSTMAN OR INSOMNIA 
</h4> <br /><br /><br />


: Route-> replace_Chain: <h4>-Connect node to longest chain if necessary to maintain validity within the network

</h4> <br />
<br /><br /><br /><br /><br />

<h3>FRONTEND</h3>

<h5>PYTHON -> NUXT.JS</h5>

: Route-> home: <h4>-HOME PAGE <h3>--displays node status</h3>

</h4> <br /><br /><br />


: Route-> dai_gen: <h4>-Allows node to generate addresses/private keys for users as well as themselves for the hosted network

</h4> <br /><br /><br />


: Route-> Mine Block: <h4>-Currently button operated on frontend but will integrate the dAIsy artificial intelligence 4/20/2021 </h4> <br />
mint_acct ='' <- must generate an address<br />
mint_key = '' <- generate key for address<br />

<br /><br /><br />

: Route-> is_valid: <h4>-Allows node to visualize validity within the network for mining

</h4><br /><br /><br />


: Route-> add_transaction: <h4>-Allows miner to receive profits from the network

</h4><br /><br /><br />


: Route-> replace_chain: <h4>-Allows miner to ensure security/validity/accurate transactions within the network

</h4><br /><br /><br />


: Route-> connected_node: <h4>-Allows miner to ensure their node is connected to network via POSTMAN/INSOMNIA

</h4><br /><br /><br />



<br /><br /><br />

<h3>NUXT.JS FRONTEND</h3>

<h5>NUXT.JS</h5> 
-Replace 8677 with node above 8685
env: {
    HOST_URL: process.env.HOST_URL || "http://127.0.0.1:8686/"
  },

  <br /><br /><br /><br /><br />

<h3>nodes.json // transactions.json will be used when requesting a post request via POSTMAN/INSOMNIA</h3><br />
<h2>to manage connected nodes run "http://127.0.0.1:8686/connect_node" with a post request via POSTMAN/INSOMNIA</h2>
