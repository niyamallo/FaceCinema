<template>
  <div class="d-flex justify-content-center">
    <div class="card d-flex" style="width: 48rem">
      <div class="card-body">
        <table class="table table-hover table-forum text-center">
          <thead>
            <tr>
              <th></th>
              <th class="text-left">Topic</th>
              <th>Comments</th>
            </tr>
          </thead>
          <Article
            v-for="article in articles" :key="article.id" :article="article" 
          />
        </table>
        <div class="text-end">
          <router-link :to="{ name: 'Create'}">
            <button class="custom-btn">글 쓰기</button>
          </router-link>
        </div>
        <!-- Pagination -->
        <div class="d-flex justify-content-center">
          <v-pagination :length="1"></v-pagination>
        </div>
      </div>
    </div>
    

  </div>
</template>

<script>
import Article from './Article.vue'

export default {
  name: 'ArticleList',
  components: {
    Article,
  },
  computed: {
    articles () {
      return this.$store.state.articles
    },
  },
}
</script>

<style scoped>
  .custom-btn {
    color: #2A2B30;
    font-weight: bold;
    border: 1px dashed #F7D54D;
    border-radius: 15px;
    padding: 5px 20px;
  }
</style>

