<template>
  <div>
    <!-- <h1>Sign Up</h1> -->
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <br>

      <input type="submit" value="SignUp">
    </form>
    <br>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      // if (!this.isValidPasswordFormat(this.password1)) {
      //   alert('비밀번호는 영문자, 숫자, 특수문자를 포함하여야 하며, 최소 8자 이상이어야 합니다.')
      //     return
      // }

      // if (this.password1 !== this.password2) {
      //   alert('비밀번호가 일치하지 않습니다.');
      //   return;
      // }

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    },
    // isValidPasswordFormat(password) {
    //   // 영어 대소문자 구분
    //   // const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+\\\|\[\]{};:'",.<>\/?]).{8,}$/
    //   const passwordRegex = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+\\\|\[\]{};:'",.<>\/?]).{8,}$/i;

    //   return passwordRegex.test(password)
    // },
  }
}
</script>

<style>

</style>