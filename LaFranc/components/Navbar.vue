<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light mb-5">
    <div class="container-fluid">
      <nuxt-link to="/" class="navbar-brand">LaFranc Testnet</nuxt-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <nuxt-link to="/home" class="nav-link">Home</nuxt-link>
          </li>
       </ul>
               <ul class="navbar-nav">
          <li class="nav-item">
            <nuxt-link to="/connect_node" class="nav-link">Connect Node</nuxt-link>
          </li>
       </ul>
                      <ul class="navbar-nav">
          <li class="nav-item">
            <nuxt-link to="/get_chain" class="nav-link">Get Chain</nuxt-link>
          </li>
       </ul>
                             <ul class="navbar-nav">
          <li class="nav-item">
            <nuxt-link to="/Validity" class="nav-link">Chain Validity</nuxt-link>
          </li>
       </ul>
                                    <ul class="navbar-nav">
          <li class="nav-item">
            <nuxt-link to="/replaced_chain" class="nav-link">Chain Replacements</nuxt-link>
          </li>
       </ul>
                     <!-- <li class="nav-item">
            <nuxt-link to="/LaFrancME" class="nav-link">Generate New Address And Private Key</nuxt-link>
         </li>  -->
          <!-- <li class="nav-item"> -->
            <!-- <nuxt-link to="/LaFrancMint" class="nav-link">Mine LaFranc-></nuxt-link> -->
          <!-- </li> -->
         
        <template v-if="!authenticated">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <nuxt-link to="/LaFrancME" class="nav-link">Generate New Address And Private Key</nuxt-link>
            </li>
            <li class="nav-item">
              <nuxt-link to="/LaFrancMint" class="nav-link">Mine LaFranc -->MUST HAVE API TO ACCESS NODE</nuxt-link>
            </li>
          </ul>
        </template>
        <!-- <template v-if="authenticated">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link">{{ user.name }}</a>
            </li>
            <li class="nav-item">
              <a @click.prevent="logout" class="nav-link">Logout</a>
            </li>
          </ul>
        </template> -->
      </div>
    </div>
  </nav>
</template>
<script>
// import { mapGetters } from "vuex";
export default {
  methods:{
    logout() {
      this.$auth.logout()
    }

  }
};
</script>
