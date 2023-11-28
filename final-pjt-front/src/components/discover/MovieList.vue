<template>
  <div>
    <div class="d-flex flex-wrap">
      <MovieCard
      v-for="movie in displayedMovies" :key="movie.id" :movie="movie" :backdropPath="movie.backdrop_path"
      class="movie-card"
      />
    </div>
    <div v-if="moviesCount" class="btn-container">
      <button class="custom-btn" @click="previousPage" :disabled="currentPage === 1">prev</button>
      <button class="custom-btn" @click="nextPage" :disabled="currentPage === totalPages">next</button>
    </div>
  </div>
</template>

<script>
import MovieCard from './MovieCard.vue'

export default {
  name: 'MovieList',
  data() {
    return {
      itemsPerPage: 15,
      currentPage: 1,
    }
  },
  components: {
    MovieCard,
  },
  props: {
    movies: Array
  },
  computed: {
    displayedMovies() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.movies.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.movies.length / this.itemsPerPage)
    },
    moviesCount() {
      return this.movies.length > this.itemsPerPage
    }
  },
  methods: {
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1
      }
      this.scrollToTop()
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1
      }
      this.scrollToTop()
    },
    scrollToTop() {
      window.scrollTo({top: 0, behavior: 'auto'})
      // window.scrollTo({top: 0, behavior: 'smooth'})
    }
  }
}
</script>

<style scoped>
  .btn-container {
    display: flex;
    justify-content: space-around;
    margin-bottom: 100px;
  }
  .movie-card {
    width: 350px;
  }
  .custom-btn {
    color: #F7D54D;
    font-weight: bold;
    border: 1px dashed #F7D54D;
    border-radius: 15px;
    padding: 5px 20px;
  }
</style>