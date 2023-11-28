<template>
  <div>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/discuss/ArticleList.vue'


export default {
  name: 'DiscussView',
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'ProfileView' })
      }
    }
  }
}
</script>

<style scoped>

</style>