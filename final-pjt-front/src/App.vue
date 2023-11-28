<template>
  <div id="app">
    <nav>
      |
      <router-link :to="{name: 'HomeView'}">Home</router-link> |
      <router-link :to="{name: 'DiscoverView'}">Discover</router-link> |
      <router-link :to="{name: 'RecommendView'}">Recommend</router-link> |
      <router-link :to="{name: 'DiscussView'}">Discuss</router-link> |
      <router-link :to="{name: 'ProfileView'}">Profile</router-link> |
      <button v-if="!isLogin" @click="openModal" class="login-button">Log In</button>
      <button v-else @click="logOut" class="logout-button">Log Out</button>
        <modal name="login-modal">
          <AccountModal @login="handleLogin" @close="closeModal" />
        </modal>
      |
    </nav>
    <router-view/>
  </div>
</template>

<script>
import AccountModal from '@/components/account/AccountModal.vue'

export default{
  components: {
    AccountModal
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    openModal() {
      this.$modal.show('login-modal')
    },
    closeModal() {
      this.$modal.hide('login-modal')
    },
    handleLogin() {
      // this.isLoggedIn = true
      this.closeModal()
    },
    logOut() {
      this.$store.dispatch('logOut')
    },
  }
}
</script>


<style>

html, body {
  background-color: #2A2B30; /* 배경 색상 설정 */
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #F7D54D;
  background-color: #2A2B30;
}

nav {
  padding: 40px 30px 50px 30px;
}

nav a {
  font-size: 150%;
  font-weight: bold;
  color: #dc8640;
}

nav a.router-link-exact-active {
  color: #c0251f;
}

.login-button {
  font-size: 150%;
  font-weight: bold;
  color: #dc8640; /* 로그인 버튼 텍스트 색상 */
}

.logout-button {
  font-size: 150%;
  font-weight: bold;
  color: #dc8640; /* 로그아웃 버튼 텍스트 색상 */
}

</style>

