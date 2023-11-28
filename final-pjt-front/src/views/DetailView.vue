<template>
  <div>
    <div class="img-container">
      <div class="movie-image" :style="getBackgroundStyle(movie.backdrop_path)"></div>
        <div class="movie-info">
          <p class="title">{{ movie.title }}</p>
          <div class="rating">
            <p class="star"><i class="bi bi-star-fill"></i></p>
            <br>
            <p class="vote-average">{{ movie.vote_average }}</p>
            <p class="release-date">/ {{ movie.release_date }}</p>
          </div>
        </div>
      </div>
    <hr>
    <div class="overview-container">
      <div class="movie-overview">{{ movie.overview }}</div>
    </div>
    <div v-if="userId">
      <!-- <button @click="likeMovie">🤍</button> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import 'bootstrap-icons/font/bootstrap-icons.css'
const API_URL = 'http://127.0.0.1:8000/movies'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: null,
    }
  },
  computed: {
    userId() {
      if (this.$store.state.user) {
        return this.$store.state.user.id
      }
    }
  },
  created() {
    const id = this.$route.params.id;
    this.fetchMovie(id)
  },
  methods: {
    async fetchMovie(id) {
      const result = await axios.get(`${API_URL}/${id}`)
      this.movie = result.data
    },
    getBackgroundStyle(posterPath) {
      const baseUrl = 'https://image.tmdb.org/t/p/original'
      return {
        backgroundImage: `url(${baseUrl + posterPath})`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: 'cover',
      }
    },
    async likeMovie() {
      const movie = this.movie
      const result = await axios.post(`${API_URL}/${this.userId}/${movie.title}/like`)
      console.log(result.data)
    },
  }
}
</script>

<style scoped>

  .hr {
    margin-top: 0%;
  }
  .img-container {
    position: relative;
    width: 80%;
    max-height: 40vh; /* 최대 높이를 40%의 뷰포트 높이로 제한 */
    padding-bottom: 40%; /* 16:9 비율에 맞게 조정 */
    margin: 0 auto; /* 가운데 정렬을 위한 margin 설정 */
  }

  .movie-image {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 5%; /* 여백 설정 */
  }

  .title {
    word-break: keep-all;
    font-size: 470%;
    font-weight: bold;
    margin-left: 5%;
  }

  .rating {
    display: flex;
    align-items: center;
    margin-left: 5%;
    margin-right: 5%; /* 별 모양 아이콘과 vote_average 사이의 여백 */
    margin-bottom: 5%;
  }

  .star {
    color: rgb(252, 252, 137);
    font-size: 250%;
  }
  .vote-average {
    font-size: 250%;
    margin-left: 5px; /* 별 모양 아이콘과 vote_average 사이의 여백 */
  }

  .release-date {
    font-size: 250%;
    margin-left: 10px; /* vote_average와 개봉일 사이의 여백 */
  }
    
  .movie-info {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    position: absolute;
    bottom: 5%;
    left: 5%;
    color: #fff;
    max-width: 80%;
  }

  .overview-container {
    position: relative;
    width: 80%;
    max-height: 40vh; /* 최대 높이를 40%의 뷰포트 높이로 제한 */
    padding-bottom: 40%; /* 16:9 비율에 맞게 조정 */
    margin: 0 auto; /* 가운데 정렬을 위한 margin 설정 */
  }  

  .movie-overview {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    /* align-items: center; */
    justify-content: center;
    margin: 5%; /* 여백 설정 */
    color: #fff;
    text-align:left;
  }

  /* 반응형 글자 크기 */
  @media (max-width: 1023px) {
    .img-container {
      width: 100%;
    }

    .overview-container {
      width: 100%;
    }
    
    .title {
      font-size: 350%;
    }

    .star {
      font-size: 150%;
    }

    .vote-average {
      font-size: 150%;
    }

    .release-date {
      font-size: 150%;
    }
  }

  @media (max-width: 768px) {
    .img-container {
      width: 100%;
    }

    .overview-container {
      width: 100%;
    }

    .title {
      font-size: 200%;
    }

    .star {
      font-size: 100%;
    }

    .vote-average {
      font-size: 100%;
    }

    .release-date {
      font-size: 100%;
    }
  }

  @media (max-width: 480px) {
    .img-container {
      width: 100%;
    }

    .overview-container {
      width: 100%;
    }

    .title {
      font-size: 150%;
    }

    .star {
      font-size: 85%;
    }

    .vote-average {
      font-size: 85%;
    }

    .release-date {
      font-size: 85%;
    }
  }
</style>