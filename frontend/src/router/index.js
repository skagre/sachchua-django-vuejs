import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Detail from '../views/Detail.vue'
import Category from '../views/Category.vue'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/detail/:id',
    name: 'Detail',
    component: Detail
  },
  {
    path: '/category/:id',
    name: 'Category',
    component: Category
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard/',
    name: 'Dashboard',
    component: Dashboard
  }
]

const router = new VueRouter({
  routes
})


export default router
