import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PerformanceView from '../views/PerformanceView.vue'
import StatisticsView from '../views/StatisticsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/performance',
      name: 'performance',
      component: PerformanceView
    },
    {
      path: '/statistics',
      name: 'statistics',
      component: StatisticsView
    }
  ]
})

export default router
