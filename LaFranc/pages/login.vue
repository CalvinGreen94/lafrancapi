<template>
  <div class="container col-md-6 mt-5">
    <h2>Login</h2>

    <br />
    <form @submit.prevent="submit">
      <div class="form-group">
        <label>Username</label>
        <input
          v-model.trim="form.address"
          type="name"
          class="form-control"
          placeholder="Username"
          autofocus
        />
        <!-- <small class="form-text text-danger" v-if="errors.email">{{
          errors.email[0]
        }}</small> -->
      </div>
      <div class="form-group">
        <label>Password </label>
        <input
          v-model.trim="form.key"
          type="password"
          class="form-label"
          placeholder="Password"
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
import axios from "~/plugins/axios";

export default {
  async asyncData() {
    let { data } = await axios.get("/mine_block");
    console.log(data.data);
    return data.data;
  },
  middleware: ['guest'],
  data() {
    return {
      form: {
        address: '',
        key: ''
      }
    }
  },
};
</script>
