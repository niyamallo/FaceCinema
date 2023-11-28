<template>
  <div class="d-flex flex-column align-items-center">
    <h3>sELecT tHe mOntH oF yOuR bIrTh bElOw</h3>

    <div class="select-container">
      <select v-model="selectedMonth" class="form-select form-select-lg mb-3">
        <option value="1">1월</option>
        <option value="2">2월</option>
        <option value="3">3월</option>
        <option value="4">4월</option>
        <option value="5">5월</option>
        <option value="6">6월</option>
        <option value="7">7월</option>
        <option value="8">8월</option>
        <option value="9">9월</option>
        <option value="10">10월</option>
        <option value="11">11월</option>
        <option value="12">12월</option>
      </select>
    </div>
    <button @click="getRecommendations" class="custom-btn">영화 추천 받기</button>
    <div v-if="isSelected" class="movies-container">
      <MovieList :movies="recommendations" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/discover/MovieList.vue'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'RecommendView',
  data() {
    return {
      recommendations: null,
      selectedMonth: null,
      isSelected: false,
    }
  },
  components: {
    MovieList
  },
  methods: {
    async getRecommendations() {
      if (!this.selectedMonth) {
        alert("원하는 달을 선택해주세요")
        return
      }
      const result = await axios.get(`${API_URL}/movies/recommend/${this.selectedMonth}/`)
      this.recommendations = result.data
      this.isSelected = true
    },
  }
}
</script>

<style scoped>
  .disaplayInput{
  display: none;
  }
  .select-container{
    width: 300px;
    margin: 30px 0;
  }
  .custom-btn {
    color: #F7D54D;
    font-weight: bold;
    border: 1px dashed #F7D54D;
    border-radius: 15px;
    padding: 10px;
    margin-bottom: 50px;
  }
  .movies-container{
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>