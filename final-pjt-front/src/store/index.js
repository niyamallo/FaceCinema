import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'
// import myModule from './modules/myModule.js'

const API_URL = 'http://127.0.0.1:8000'

const createSessionStorageState = (options) => {
  const persistedState = createPersistedState({
    storage: {
      getItem: (key) => sessionStorage.getItem(key),
      setItem: (key, value) => sessionStorage.setItem(key, value),
      removeItem: (key) => sessionStorage.removeItem(key),
    },
    ...options,
  });
  return persistedState;
};

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: null,
    articles: null,
    token: null,
    user: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SET_MOVIES(state, movies) {
      state.movies = movies
    },
    SET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'DiscussView'})
    },
    REMOVE_TOKEN(state) {
      state.token = null
      state.user = null
    },
    SET_USER(state, user) {
      state.user = user
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
      .then((res) => {
          context.commit('SET_MOVIES', res.data)
        })
      .catch((err) => console.log(err))
    },
    async getUserInfo(context, token) {
      axios.defaults.headers.common['Authorization'] = `Token ${ token }`
      const result = await axios.get(`${API_URL}/accounts/user/`)
      context.commit('SET_USER', result.data)
    },
    async signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      
      const result = await axios.post(`${API_URL}/accounts/signup/`, {
        username, password1, password2
      })
      context.commit('SAVE_TOKEN', result.data.key)
      await context.dispatch('getUserInfo', result.data.key)
    },
    async logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      
      const result = await axios.post(`${API_URL}/accounts/login/`, {
        username, password
      })
      context.commit('SAVE_TOKEN', result.data.key)
      await context.dispatch('getUserInfo', result.data.key)
    },
    logOut(context) {
      context.commit('REMOVE_TOKEN')
      location.reload()
    },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/communities`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
          context.commit('SET_ARTICLES', res.data)
        })
      .catch((err) => console.log(err))
    }
  },
  // modules: {
  //   myModule,
  // }
  plugins: [
    createSessionStorageState()
  ],
})
