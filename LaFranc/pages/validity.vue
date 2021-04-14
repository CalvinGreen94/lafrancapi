<template>
  <div>
    <h1>{{message}}</h1>
    <p>Mint LaFranc</p>
  </div>
</template>

<script>
import axios from '~/plugins/axios'
export default {
  async asyncData () {
    let {data} = await axios.get('/is_valid')
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