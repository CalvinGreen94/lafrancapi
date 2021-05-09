<template>
  <div>
    <p>Welcome To The LaFranc Blockchain ecosystem</p>
    Current Blockchain Information <br />
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <material-card color="success" elevation="12" title="Connexion">
              <v-card-text>
                <h1>{{ message }}</h1>
              </v-card-text>
            </material-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </div>
</template>

<script>
import axios from "~/plugins/axios";
export default {
  async asyncData() {
    let { data } = await axios.get("/get_chain");
    console.log(data.data);
    return data.data;
  },
  head() {
    return {
      title: "LaFranc Home"
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
