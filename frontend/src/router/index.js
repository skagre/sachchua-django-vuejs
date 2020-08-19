import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Detail from '../views/Detail.vue'
import Category from '../views/Category.vue'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import DashboardProfile from '../views/DashboardProfile.vue'
import DashboardBooks from '../views/DashboardBooks.vue'
import DashboardCategories from '../views/DashboardCategories.vue'
import AddBook from '../views/AddBook.vue'
import EditBook from '../views/EditBook.vue'

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
    component: Login,
    meta: {
      auth: false
    },
  },
  {
    path: '/dashboard/',
    name: 'Dashboard',
    component: Dashboard,
    children: [
      {
        path: 'profile',
        component: DashboardProfile
      },
      {
        path: 'books',
        component: DashboardBooks
      },
      {
        path: 'categories',
        component: DashboardCategories
      },
      {
        path: 'addbook',
        component: AddBook
      },
      {
        path: 'editbook/:id',
        component: EditBook
      },
    ]
  }
]

const router = new VueRouter({
  routes
})


export default router
