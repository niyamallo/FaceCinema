<template>
  <div class="discover-container">
    <MovieList :movies="movies" />

  </div>
</template>

<script>
import MovieList from '@/components/discover/MovieList.vue'

export default {
  name: 'DiscoverView',
  components: {
    MovieList
  },
  computed: {
    movies () {
      return this.$store.state.movies
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style scoped>
.discover-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* height: 100vh; */
  padding-left: 100px;
}
</style>