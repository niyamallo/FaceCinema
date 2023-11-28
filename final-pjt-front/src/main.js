import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueJSModal from 'vue-js-modal'
import vuetify from './plugins/vuetify'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.use(VueJSModal)
Vue.use(BootstrapVue)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
