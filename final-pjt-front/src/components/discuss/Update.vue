<template>
  <div>
    <h3>게시글 수정하기</h3>
    <div class="form-container d-flex justify-content-center m-auto pt-5">
      <form @submit.prevent="updateArticle" class="actual-form">
        <div class="form-outline mb-4 input-box">
          <input type="text" v-model="title" class="form-control" placeholder="Title"/>
        </div>

        <div class="form-outline mb-4 input-box">
          <textarea v-model="content" class="form-control" rows="4" placeholder="Content"></textarea>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4 custom-btn">
          수정하기
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
const API_URL = 'http://127.0.0.1:8000'

export default {
 name: 'Update',
 data() {
    return {
      articleId: null, // 수정할 게시글의 ID
      title: '',
      content: ''
    };
  },
  created() {
    this.articleId =this.$route.params.id
    this.fetchArticle(); // 페이지 진입 시 게시글 데이터 불러오기
  },
  methods: {
    fetchArticle() {
      axios.get(`${API_URL}/communities/${this.articleId}`)
        .then(response => {
          this.title = response.data.title;
          this.content = response.data.content;
        })
        .catch(error => {
          console.error('게시글 불러오기 실패:', error);
        });
    },
    updateArticle() {
      axios.put(`${API_URL}/communities/${this.articleId}/`, {
        title: this.title,
        content: this.content
      }, {
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(response => {
          console.log('게시글 수정 완료:', response.data);
          router.push({name : 'Detail', id: this.articleId});
        })
        .catch(error => {
          console.error('게시글 수정 실패:', error);
        });
    }
  }
}
</script>

<style scoped>
.actual-form {
  width: 50%;
}
.input-box {
  border: 2px dashed #F7D54D;
  border-radius: 15px;
  /* color: white !important; */
}
.form-control {
  background: transparent;
  border: none;
  color: white;
}
.custom-btn {
  background: #F7D54D;
  color: #2A2B30;
  font-weight: bold;
  border: none;
  border-radius: 15px;
}
</style>