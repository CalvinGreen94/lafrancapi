<template>
  <div class="container col-md-6 mt-5">
    <h2>Register</h2>

    <br />
    <form @submit.prevent="submit">


     <div class="form-group">
        <label>wallet address</label>
        <input
          v-model.trim="form.name"
          type="text"
          class="form-control"
          placeholder="Enter address"
        />
        <!-- <small class="form-text text-danger" v-if="errors.name">{{
          errors.name[0]
        }}</small> -->
      </div>
     <div class="form-group">
        <label>private key</label>
        <input
          v-model.trim="form.password"
          type="text"
          class="form-control"
          placeholder="Enter password"
        />
        <!-- <small class="form-text text-danger" v-if="errors.name">{{
          errors.name[0]
        }}</small> -->
      </div>



      <button type="submit" class="btn btn-primary">Register</button>
    </form>
    <p>Thank you for signing up !</p>
    <p>Already Have an account ? <nuxt-link to="/login">Login</nuxt-link></p>
  </div>
</template>
<script>
export default {
  middleware: ['guest'],

  data() {
    return {
      form: {
        // email: '',
        name: '',
        password: ''
      }
    }
  },
  methods: {
    async submit() {
      await this.$axios.$post('register', this.form);
      await this.$auth.loginWith('local', {
        data: {
          name: this.form.name,
          password: this.form.password
        }
      });
      this.$router.push({
        path: this.$route.query.redirect || "http://127.0.0.1:8000/sakujoooCloud"
      });
    }
  }
};
</script>
