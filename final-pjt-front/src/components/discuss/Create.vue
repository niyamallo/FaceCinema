<template>
  <div>
    <h5>게시글 작성하기</h5>
    <div class="form-container d-flex justify-content-center m-auto pt-5">
      <form class="actual-form">
        <div @submit.prevent="createArticle" class="form-outline mb-4 input-box">
          <input type="text" v-model="title" class="form-control" placeholder="Title"/>
        </div>

        <div class="form-outline mb-4 input-box">
          <textarea v-model="content" class="form-control" rows="4" placeholder="Content"></textarea>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4 custom-btn">
          작성하기
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Create',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/communities/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: { title, content },
      })
      .then(() => {
        this.$router.push({name: 'DiscussView'})
      })
      .catch((err) => {
        console.log(err)
      })
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