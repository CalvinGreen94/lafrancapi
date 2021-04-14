<template>
  <div>
        <p>Full Chain <br>    
</p>
    <h1>{{message}}</h1> 

  </div>
</template>

<script>
import axios from '~/plugins/axios'
export default {
  async asyncData () {
    let {data} = await axios.get('/get_chain')
    console.log(data.data)
    return data.data
  },

  head () {
    return {
      title: 'LaFranc Blockchain'
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