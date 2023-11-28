<template>
  <div>
    <v-card class="mx-auto" max-width="344" @mouseover="reveal = true">
      <div class="card" :style="{ backgroundImage: 'url(' + getImageUrl() + ')', backgroundSize: '100% auto'}">
        <v-card-text class="title-container">
          <p class="text-h4 text--primary">{{ movie.title }}</p>
        </v-card-text>
      </div>

      <v-expand-transition>
        <v-card
          v-if="reveal"
          class="v-card--reveal"
          style="height: 100%;"
          @mouseleave="reveal = false"
          @click="goToDetail"
        >
          <v-card-text class="pb-0">
            <p class="detail-title">{{ movie.title }}</p>
            <p class="overview-container"> {{ movie.overview }}</p>
          </v-card-text>
        </v-card>
      </v-expand-transition>
    </v-card>

  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  data() {
    return {
      reveal: false
    }
  },
  props: {
    movie: Object,
    backdropPath: String,
  },
  methods: {
    goToDetail() {
      this.$router.push({ name: 'DetailView', params: { id: this.movie.id }})
    },
    getImageUrl() {
      return 'https://image.tmdb.org/t/p/original' + this.backdropPath;
    }
  },
}
</script>

<style scoped>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
  background-color: #2A2B30;
}

.card {
  height: 190px;
  text-align: end;
  margin-bottom: 30px;
}

.title-container {
  text-align: end;
  margin-bottom: 10px;
  color: #F7D54D;
  font-weight: bold;
  font-size: 1rem;
}

/* detail card */
.detail-title {
  color: #F7D54D;
  font-weight: bold;
  font-size: 1.3rem;
  margin-top: 10px;
}
.overview-container {
  line-height: 1.5;
  max-height: 4.5rem;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  color: #F7D54D;
  margin-top: 40px;
}
</style>