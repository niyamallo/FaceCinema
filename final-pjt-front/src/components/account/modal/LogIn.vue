<template>
  <div>
    <!-- <h1>Log In</h1> -->
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>
      <br>
      
      <input type="submit" value="logIn">
    </form>
    <br>
    <GoogleLogin :params="googleParams" :onSuccess="googleSuccess">
      <p>Continue with Google</p>
    </GoogleLogin>
  </div>

</template>

<script>
import GoogleLogin from 'vue-google-login'
// const clientId = process.env.CLIENT_ID

export default {
  name: 'LogIn',
  data() {
    return {
      username: null,
      password: null,
      // googleParams: {
      //   // client_id: clientId
      //   client_id: "180416682250-pfkesuimbj2v66kk08k2udrcrgtum9np.apps.googleusercontent.com"
      // },
    }
  },
  components: {
    GoogleLogin,
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('logIn', payload)

    },
    googleSuccess(googleUser) {
      console.log(googleUser)
    }
  }
}
</script>

<style>

</style>