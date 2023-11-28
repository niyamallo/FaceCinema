<template>
  <div class="d-flex justify-content-center">
    <div class="card" style="width: 48rem">
      <div class="card-body">
        <div class="d-flex mb-3 align-items-center">
          <img src="https://mdbcdn.b-cdn.net/img/new/avatars/18.webp" class="border rounded-circle me-2"
            alt="Avatar" style="height: 40px" />
          <div>
            <p href="" class="mb-0 dali-color">
              <strong>{{ article?.userName }}</strong>
            </p>
            <p href="" class="mb-0 dali-color">
              <small>{{ date }}</small>
            </p>
          </div>
          <div>
            <h3 id="article-title" class="dali-color">
              {{ article?.title }}
            </h3>
          </div>
        </div>
        <div class="dali-color">
          {{ article?.content }}
        </div>
      </div>
      <div class="d-flex justify-content-end">
        <router-link :to="{ name: 'Update', params: { id: article.id }}"
        class="link edit"
        >
          수정
        </router-link>
        <button @click="deleteArticle" class="edit">삭제</button>
      </div>
        <!-- 버튼 -->
        <div class="d-flex justify-content-between text-center border-top border-bottom mb-4">
          <button type="button" class="btn btn-link btn-lg" data-mdb-ripple-color="dark">
            <Icon icon="ant-design:like-outlined" />
          </button>
          <button type="button" class="btn btn-link btn-lg" data-mdb-ripple-color="dark">
            <Icon icon="ant-design:dislike-outlined" />
          </button>
          <button type="button" class="btn btn-link btn-lg" data-mdb-ripple-color="dark">
            <Icon icon="uil:share" />
          </button>
        </div>
        
        <div class="card-body dali-color">
          <!-- 댓글 -->
          <div class="comment-header">
            <h5>Comments</h5>
          </div>
          <Comment
          v-for="comment in comments" :key="comment.id" :comment="comment"
          />
          <form @submit.prevent="createComment">
            <div class="d-flex mb-3">
              <Icon icon="bxs:user" class="user-icon"/>
              <div class="form-outline w-100">
                <textarea class="form-control" rows="2" v-model.trim="content" placeholder="댓글을 남겨주세요"></textarea>
              </div>
            <button type="submit" class="submit-btn">댓글 쓰기</button>
            </div>
          </form>

        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
import { Icon } from '@iconify/vue2'
import Comment from '@/components/discuss/Comment.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Datail',
  components: {
    Comment,
    Icon,
  },
  data() {
    return {
      article: null,
      content: null,
      comments: null,
    }
  },
  computed: {
    date() {
      const date = new Date(this.article?.created_at)
      return date.toLocaleDateString()
    }
  },
  created() {
    this.getArticleDetail()
    this.getComments()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/communities/${ this.$route.params.id }/`,
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteArticle() {
      axios.delete(`${API_URL}/communities/${this.article.id}/`)
        .then(response => {
          router.push({name : 'DiscussView'})
        })
        .catch(error => {
          alert('게시글 삭제에 실패했습니다. 다시 시도해주세요.')
        });
    },
    getComments() {
      axios({
        method: 'get',
        url: `${API_URL}/communities/${ this.$route.params.id }/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createComment() {
      const content = this.content
      if (!content) {
        alert('댓글을 입력해주세요.')
        return
      }
      console.log(this.$store.state.token)
      axios({
        method: 'post',
        url: `${API_URL}/communities/${this.article.id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content,
        },
      })
      .then((res) => {
        this.content = ''
        // this.$router.push({name : 'Detail', id: this.article.id})
        location.reload()
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
.card {
  text-align: unset;
}
#article-title{
  margin-left: 50px;
}
.link {
  text-decoration: none;
}
.edit {
  color: gray;
  margin-right: 10px;
}
.submit-btn {
  width: 50px;
  margin-left: 15px;
  border: 1px dashed #F7D54D;
  color: #2A2B30;
  border-radius: 15px;
  padding: 3px;
}
.comment-header {
  text-align: left;
}
.user-icon {
    margin-right: 10px;
    height: 50px;
}
.dali-color {
  color: #2A2B30;
}
</style>