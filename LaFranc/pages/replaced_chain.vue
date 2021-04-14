<template>
  <div>
        <p>Replaced LaFranc Chains <br>   Detect If Node is Connected to longest chain
</p>
    <h1>{{message}}</h1> 

  </div>
</template>

<script>
import axios from '~/plugins/axios'
export default {
  async asyncData () {
    let {data} = await axios.get('/replace_chain')
    console.log(data.data)
    return data.data
  },

  head () {
    return {
      title: 'Detect Node Status'
    }
  }
}
</script>

<style>
h1 {
  font-size: 40px;
}
p {
  font-size: 20px;
}
</style>