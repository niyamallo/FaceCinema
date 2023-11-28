<template>
  <div v-if="isLogin">
    <UserInfo />
  </div>

  <div v-else>
    <AccountModal />
  </div>
</template>

<script>
import UserInfo from '@/components/account/UserInfo.vue'
import AccountModal from '@/components/account/AccountModal.vue'

export default {
  name: 'ProfileView',
  components: {
    UserInfo,
    AccountModal,
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
      this.isLoggedIn = true
      this.closeModal()
    },
  }
}
</script>

<style>

</style>