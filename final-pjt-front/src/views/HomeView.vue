<template>
  <div>
    <router-link :to="{ name: 'DiscoverView'}">
      <button class="enter-button">EnteR and Get yoUr owN pOstER</button>
      <br>
      <img class="main-image" src = "@/assets/images/el-salvador-dali-g680984f6a_1920.png" />
    </router-link>
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'

export default {
  name: 'HomeView',
  created() {
    this.callDjango()
  },
  methods: {
    callDjango() {
      axios.get(`${API_URL}/movies/make_database/`)
      .then(() => console.log('success'))
    }
  }
}
</script>

<style scoped>
  .main-image {
    max-width: 27%;
    max-height: 27%;
    display: block;
    margin: 0 auto 5%;
  }
  .enter-button {
    font-size: 300%;
  }
</style>