import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView.vue'

import DiscoverView from '@/views/DiscoverView.vue'

import RecommendView from '@/views/RecommendView.vue'
import DetailView from '@/views/DetailView.vue'

import DiscussView from '@/views/DiscussView.vue'
import Create from '@/components/discuss/Create.vue'
import Detail from '@/components/discuss/Detail.vue'
import Update from '@/components/discuss/Update.vue'

import ProfileView from '@/views/ProfileView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/discover',
    name: 'DiscoverView',
    component: DiscoverView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/discuss',
    name: 'DiscussView',
    component: DiscussView,
  },
  {
    path: '/discuss/create',
    name: 'Create',
    component: Create
  },
  {
    path: '/discuss/:id',
    name: 'Detail',
    component: Detail
  },
  {
    path: '/discuss/:id/update',
    name: 'Update',
    component: Update
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
