<template>
  <div>
        <p>Conected Nodes<br>    Must be a connected node via LaFranc API
</p>
    <h1>{{message}}</h1> 

  </div>
</template>

<script>
import axios from '~/plugins/axios'
export default {
  async asyncData () {
    let {data} = await axios.get('/connect_node')
    console.log(data.data)
    return data.data
  },

  head () {
    return {
      title: 'Mine LaFranc Blockchain'
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