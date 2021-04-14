<template>
  <div class="center">
    <p>Generate LaFranc Address</p>
    <h3>Mint LaFranc via LaFranc testnet Generator.</h3>
    <br />Please Use the Brave browser or Google Chrome when using this
    application to be able to access each feature as well as swap between
    various ERC20 tokens/contracts while maintaining security and access to
    Web3.0 features.
    <p>WELCOME TO THE LaFranc Token Generator.</p>
    <br />
    <p>
      Install a metamask extension for your ERC20 transactions. <br />
      Click the 'Generate LaFranc address' button below to get started
    </p>
    <p>
      AFTER ADDRESS HAS BEEN GENERATED MAKE SURE YOU ARE INTERACTING WITH THE
      TESTNET LaFranc CONTRACT AT THIS ERC20 ADDRESS
    </p>
    0x47edc4747A04e968AdfCEefE97af25a61b5B9A9C .
    <br />
    <p>
      INSIDE OF YOUR NEW GENERATED ERC20 ADDRESS CLICK ADD TOKEN -> CUSTOM TOKEN
      -> 'CONTRACT ADDRESS' .
      <br />
    </p>

    <p>
      The basis of LaFranc is to continuously provide liquidity to token holders
      within the ERC20 ecosystem, LaFranc-DAI protocol will make it simple for
      anyone to gain access to liquid markets.
      <!-- <form action="/dai_gen" method="post">
      <button type="submit" class="btn btn-primary btn-block btn-large">
        Click here to Generate a LaFranc Address
      </button> -->

      <br />
    </p>

    <p>
      AFTER LAFRANC ADDRESS IS GENERATED YOU WILL NEED TESTNET ETHEREUM. RECIEVE
      5 FREE TEST ETH <br />
    </p>

    <p align-center>
      <a href="https://faucet.dimensions.network/" target="_blank">
        <button type="submit" class="btn btn-primary">
          ROPSTEN FAUCET
        </button>
      </a>
    </p>
    <br />

    To maintain liquidity, stake within C-Force and LaFranc token pairs and take
    advantage of learning how to operate the testnet before mainnet swap.
    <!-- <h5> -->
    When a holder takes funds from the contract a portion of the coins will
    automatically be burned into non-accessible wallets to help increase demand
    <br />as well as into the Uniswap contract pairs to provide liquidity.<br />
    <!-- </h5> -->
    YOUR LAFRANC WALLET INFORMATION: <br />
    <p></p>

    <p align-center>{{ message }}</p>

    <a href="/login" target="_blank">
      <button type="submit" class="btn btn-primary">
        Login in with New Address And Private key
      </button>
    </a>
  </div>
</template>

<script>
import axios from "~/plugins/axios";
export default {
  async asyncData() {
    let { data } = await axios.get("/dai_gen");
    console.log(data.data);
    return data.data;
  },
  head() {
    return {
      title: "Generate Access to LaFranc"
    };
  }
};
</script>

<style>
h1 {
  font-size: 40px;
}
p {
  font-size: 20px;
}
</style>
