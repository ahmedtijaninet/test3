import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/a-propos',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/offres',
      name: 'offers',
      component: () => import('../views/OffersView.vue'),
    },
    {
      path: '/coworking',
      name: 'coworking',
      component: () => import('../views/CoworkingView.vue'),
    },
    {
      path: '/consulting',
      name: 'consulting',
      component: () => import('../views/ConsultingView.vue'),
    },
    {
      path: '/suite',
      name: 'suite',
      component: () => import('../views/SuiteView.vue'),
    },
    {
      path: '/communaute',
      name: 'community',
      component: () => import('../views/CommunityView.vue'),
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/ContactView.vue'),
    },
    {
      path: '/checkout',
      name: 'checkout',
      component: () => import('../views/CheckoutView.vue'),
    },
    {
      path: '/confirmation',
      name: 'confirmation',
      component: () => import('../views/ConfirmationView.vue'),
    },
  ],
})

export default router
