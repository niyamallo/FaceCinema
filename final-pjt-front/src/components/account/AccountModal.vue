<template>
  <div class="login-popup">
    <h1>Log in or Sign up here.</h1>
    <div
      v-for="(tab, index) in tabs"
      :key="index"
      class="tab"
      :class="{ active: activeTab === index }"
      @click="changeTab(index)"
    >
      {{ tab.name }}
    </div>
    <div class="tab-content">
      <component :is="activeComponent"></component>
    </div>
  </div>
</template>

<script>
import LogIn from '@/components/account/modal/LogIn.vue'
import SignUp from '@/components/account/modal/SignUp.vue'

export default {
  name: 'accountModal',
  components: {
    LogIn,
    SignUp,
  },
  data() {
    return {
      tabs: [
        { name: 'LogIn', component: 'LogIn'},
        { name: 'SignUp', component: 'SignUp'},
      ],
      activeTab: 0,
    }
  },
  computed: {
    activeComponent() {
      return this.tabs[this.activeTab].component;
    }
  },
  methods: {
    changeTab(index) {
      this.activeTab = index;
    }
  }
}
</script>

<style scoped>
.login-popup {
  background-color: rgb(179, 132, 80);
}

.tab {
  display: inline-block;
  padding: 10px 20px;
  cursor: pointer;
}

.active {
  background-color: #eee;
}

.tab-content {
  margin-top: 20px;
}
</style>