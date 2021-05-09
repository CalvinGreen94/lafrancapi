<template>
  <div class="container col-md-6 mt-5">
    <h2>Login</h2>

    <br />
    <form @submit.prevent="submit">
      <div class="form-group">
        <label>Wallet Address</label>
        <input
          v-model.trim="form.name"
          type="name"
          class="form-control"
          placeholder="wallet_address"
          autofocus
        />
        <!-- <small class="form-text text-danger" v-if="errors.email">{{
          errors.email[0]
        }}</small> -->
      </div>
      <div class="form-group">
        <label>Private key </label>
        <input
          v-model.trim="form.password"
          type="password"
          class="form-label"
          placeholder="private_key"
        />
        <!-- <small class="form-text text-danger" v-if="errors.password">{{
          errors.password[0]
        }}</small> -->
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
    <br />
    <p>
      Create account if needed <nuxt-link to="/LaFrancMe">Register</nuxt-link>
    </p>
  </div>
</template>



<script>
export default {
  middleware: ['guest'],
  data() {
    return {
      form: {
        name: '',
        password: ''
      }
    }
  },
  methods: {
    async submit() {
      await this.$auth.loginWith("local", {
        data: this.form
      });
      this.$router.push({
        path: this.$route.query.redirect || "http://127.0.0.1:8000/image-upload"
      });
    }
  }
};
</script>